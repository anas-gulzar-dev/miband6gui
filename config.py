# Configuration file for Biosensor Data Capture Tool
# This file loads configuration from environment variables (.env file)

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure Computer Vision API Configuration
# Load Azure credentials from environment variables
AZURE_API_KEY = os.getenv('AZURE_API_KEY')
AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT')

# Application Settings
DEFAULT_CAPTURE_INTERVAL = int(os.getenv('DEFAULT_CAPTURE_INTERVAL', '60'))
SCREENSHOTS_FOLDER = os.getenv('SCREENSHOTS_FOLDER', 'screenshots')

# Window Detection Settings
SCRCPY_WINDOW_TITLES = os.getenv('SCRCPY_WINDOW_TITLES', 'scrcpy,Mi Band,Android,Xiaomi').split(',')

# OCR API Settings
OCR_LANGUAGE = os.getenv('OCR_LANGUAGE', 'en')
DETECT_ORIENTATION = os.getenv('DETECT_ORIENTATION', 'true').lower() == 'true'

# USB Stability Settings
# Set to 'true' to enable screenshot auto-deletion (may cause USB disconnects)
# Set to 'false' to preserve screenshots and improve USB stability
ENABLE_AUTO_DELETE_SCREENSHOTS = os.getenv('ENABLE_AUTO_DELETE_SCREENSHOTS', 'false').lower() == 'true'

# Window Size Validation Settings
# Minimum window size for capture - set to smaller values for small screens
MIN_WINDOW_WIDTH = int(os.getenv('MIN_WINDOW_WIDTH', '10'))
MIN_WINDOW_HEIGHT = int(os.getenv('MIN_WINDOW_HEIGHT', '10'))
# Set to 'false' to disable warnings for small windows
SHOW_SMALL_WINDOW_WARNING = os.getenv('SHOW_SMALL_WINDOW_WARNING', 'true').lower() == 'true'
# Threshold for what's considered a "small" window (shows warning but allows capture)
SMALL_WINDOW_WARNING_WIDTH = int(os.getenv('SMALL_WINDOW_WARNING_WIDTH', '10'))
SMALL_WINDOW_WARNING_HEIGHT = int(os.getenv('SMALL_WINDOW_WARNING_HEIGHT', '10'))

# Validate required environment variables
if not AZURE_API_KEY:
    print("ERROR: AZURE_API_KEY not set in .env file")
    print("Please copy .env.example to .env and set your actual Azure API key")
    
if not AZURE_ENDPOINT:
    print("ERROR: AZURE_ENDPOINT not set in .env file")
    print("Please copy .env.example to .env and set your actual Azure endpoint")