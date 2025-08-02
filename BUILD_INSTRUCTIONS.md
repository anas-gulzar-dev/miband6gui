# Grace Biosensor Capture - Build Instructions

This guide will help you create a standalone executable for Grace Biosensor Capture with your custom `app_icon.png` icon.

## Prerequisites

1. **Python 3.7+** installed on your system
2. **All dependencies** installed (run `pip install -r requirements.txt` or `pip install -r windows_requirements.txt`)
3. **PyInstaller** (will be installed automatically if not present)
4. **app_icon.png** file in the project directory

## Quick Build (Recommended)

### Option 1: Using the Batch File (Windows)
1. Double-click `build.bat`
2. The script will automatically:
   - Check requirements
   - Install PyInstaller if needed
   - Build the executable
   - Show results

### Option 2: Using the Python Script
```bash
python build_executable.py
```

## Manual Build

If you prefer to build manually:

```bash
# Install PyInstaller if not already installed
pip install PyInstaller

# Build the executable
pyinstaller --clean --onefile --windowed --name=Grace-Biosensor-Capture --icon=app_icon.png --add-data="app_icon.png;." main.py
```

## Build Process

The build process includes:

1. **Requirements Check** - Verifies all dependencies are installed
2. **Icon Verification** - Confirms your `app_icon.png` exists and is valid
3. **Cleanup** - Removes old build files
4. **Version File** - Creates Windows version information
5. **Executable Creation** - Builds the standalone .exe file
6. **Verification** - Confirms the build was successful

## Output

After successful build:
- **Executable**: `dist/Grace-Biosensor-Capture.exe`
- **Size**: Approximately 50-100MB (includes all dependencies)
- **Icon**: Your custom `app_icon.png` will be embedded

## Icon Requirements

Your `app_icon.png` should be:
- **Format**: PNG
- **Size**: Recommended 256x256 pixels or larger
- **Quality**: High resolution for best results
- **Location**: In the same directory as `main.py`

## Troubleshooting

### Common Issues

1. **"PyInstaller not found"**
   - Solution: Run `pip install PyInstaller`

2. **"Icon file not found"**
   - Ensure `app_icon.png` is in the project directory
   - Check file permissions

3. **"Import errors during build"**
   - Install missing dependencies: `pip install -r requirements.txt`
   - For Windows: `pip install -r windows_requirements.txt`

4. **"Executable not showing custom icon"**
   - Verify `app_icon.png` is a valid PNG file
   - Check file size (should be > 1KB)
   - Try rebuilding with `--clean` flag

### Manual Icon Verification

Test if your icon works:
```python
from PyQt5.QtGui import QIcon
import os

icon_path = "app_icon.png"
if os.path.exists(icon_path):
    icon = QIcon(icon_path)
    print(f"Icon valid: {not icon.isNull()}")
    print(f"File size: {os.path.getsize(icon_path)} bytes")
else:
    print("Icon file not found")
```

## Build Outputs

After building, you'll find:
- `dist/Grace-Biosensor-Capture.exe` - Your standalone executable
- `build/` - Temporary build files (can be deleted)
- `Grace-Biosensor-Capture.spec` - PyInstaller specification file

## Distribution

The executable in `dist/` is completely standalone and can be:
- Copied to other Windows computers
- Run without Python installation
- Distributed to users
- Added to Windows startup folder

## Notes

- The first run might take a few seconds as the executable unpacks
- All dependencies are included in the executable
- The `app_icon.png` is embedded in the executable
- The executable will create necessary folders (`screenshots/`, etc.) on first run
- Your `.env` file (if present) should be in the same directory as the executable

## Support

If you encounter issues:
1. Check the error messages in the console
2. Verify all dependencies are installed
3. Ensure `app_icon.png` is valid
4. Try rebuilding with `--clean` flag
