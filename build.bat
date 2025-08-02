@echo off
echo ======================================
echo Grace Biosensor Capture - Build Script
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip is not available
    echo Please ensure pip is installed and try again
    pause
    exit /b 1
)

REM Install PyInstaller if not present
echo Checking for PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install PyInstaller
    if errorlevel 1 (
        echo ERROR: Failed to install PyInstaller
        pause
        exit /b 1
    )
)

REM Run the build script
echo.
echo Running build script...
python build_executable.py

if errorlevel 1 (
    echo.
    echo BUILD FAILED!
    echo Check the error messages above for details.
    pause
    exit /b 1
)

echo.
echo BUILD COMPLETED SUCCESSFULLY!
echo.
echo The executable is located in the 'dist' folder.
echo You can now run Grace-Biosensor-Capture.exe
echo.
pause
