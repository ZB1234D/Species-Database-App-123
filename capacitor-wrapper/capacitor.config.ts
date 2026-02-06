import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.raimatak.speciesdb',
  appName: 'Species Database App',
  webDir: 'www',
  plugins: {
    SplashScreen: {
      launchShowDuration: 1500,
      launchAutoHide: true,
      backgroundColor: '#0b5c37',
      androidScaleType: 'CENTER_CROP',
      showSpinner: false
    }
  }
};

export default config;
