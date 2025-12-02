import json
import pandas as pd
from jsonschema import validate, ValidationError
from pydantic import ValidationError as PydanticValidationError
from models import SpeciesRecord
from openpyxl import Workbook

# ----- Clean Sr_No Function -----
def clean_sr_no(df: pd.DataFrame, prefix: str = "SPC-", padding: int = 4) -> pd.DataFrame:
    """
    Generate unique prefix-based Sr_No for all rows.
    """
    df = df.copy()
    df["Sr_No"] = [f"{prefix}{str(i).zfill(padding)}" for i in range(1, len(df) + 1)]
    return df

# ----- Dataset Audit Class -----
class DatasetAudit:

    def __init__(self, df: pd.DataFrame, schema_path: str, prefix: str = "SPC-"):
        # Step 1: Clean Sr_No first
        df = clean_sr_no(df, prefix=prefix)
        self.df = df
        self.schema = json.load(open(schema_path))
        self.report = {
            "missing_values": {},
            "duplicates": [],
            "schema_errors": [],
            "pydantic_errors": [],
            "extra_fields": []
        }

    # Check missing values
    def check_missing_values(self):
        self.report["missing_values"] = self.df.isna().sum().to_dict()

    # Check duplicates
    def check_duplicates(self):
        dup = self.df[self.df.duplicated()]
        self.report["duplicates"] = dup.index.tolist()

    # JSON Schema validation
    def validate_json_schema(self):
        for idx, row in self.df.iterrows():
            try:
                validate({k: v for k, v in row.items() if pd.notna(v)}, self.schema)
            except ValidationError as e:
                self.report["schema_errors"].append({"row": idx, "error": str(e)})

    # Pydantic validation
    def validate_pydantic(self):
        for idx, row in self.df.iterrows():
            try:
                SpeciesRecord(**row.to_dict())
            except PydanticValidationError as e:
                self.report["pydantic_errors"].append({"row": idx, "error": e.errors()})

    # Detect extra columns
    def detect_extra_fields(self):
        expected = set(self.schema["properties"].keys())
        actual = set(self.df.columns)
        self.report["extra_fields"] = list(actual - expected)

    # Run all checks
    def run(self):
        self.check_missing_values()
        self.check_duplicates()
        self.validate_json_schema()
        self.validate_pydantic()
        self.detect_extra_fields()
        return self.report

# ----- Excel Export -----
def write_clean_excel(df: pd.DataFrame, filename="cleaned_species_dataset.xlsx") -> str:
    wb = Workbook()
    ws = wb.active
    ws.append(df.columns.tolist())
    for row in df.itertuples(index=False, name=None):
        ws.append(list(row))
    wb.save(filename)
    return filename
