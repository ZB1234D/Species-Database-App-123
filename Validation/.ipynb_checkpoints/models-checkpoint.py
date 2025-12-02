{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0fa269f3-63fb-47bf-b9a5-f538d5d085eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pydantic import BaseModel\n",
    "from typing import Optional\n",
    "\n",
    "class SpeciesRecord(BaseModel):\n",
    "    Sr_No: str\n",
    "    Scientific_name: str\n",
    "    Etymology: Optional[str]\n",
    "    Common_name: Optional[str]\n",
    "    Habitat: Optional[str]\n",
    "    Phenology: Optional[str]\n",
    "    Identification: Optional[str]\n",
    "    Characters: Optional[str]\n",
    "    Leaf_type: Optional[str]\n",
    "    Fruit_Type: Optional[str]\n",
    "    Seed_Germination: Optional[str]\n",
    "    Pest: Optional[str]\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
