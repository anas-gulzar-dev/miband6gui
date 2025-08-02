#!/usr/bin/env python3
"""
Grace Biosensor Capture - Build Executable Script
Creates a standalone executable with custom icon using PyInstaller
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def check_requirements():
    """Check if all required dependencies are installed"""
    required_packages = [
        'PyInstaller',
        'PyQt5',
        'requests',
        'Pillow',
        'pyautogui',
        'mss',
        'pywinctl'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.lower().replace('-', '_'))
            print(f"✅ {package} is installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} is NOT installed")
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Please install them using:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

def clean_build_directories():
    """Clean up previous build directories"""
    directories_to_clean = ['build', 'dist', '__pycache__']
    
    for directory in directories_to_clean:
        if os.path.exists(directory):
            print(f"🧹 Cleaning {directory}...")
            shutil.rmtree(directory)
    
    print("✅ Build directories cleaned")

def verify_icon_file():
    """Verify that the icon file exists and is valid"""
    # Check for ICO file first (better for Windows)
    ico_path = "app_icon.ico"
    png_path = "app_icon.png"
    
    icon_path = None
    
    # Prefer ICO file if available
    if os.path.exists(ico_path):
        icon_path = ico_path
        print(f"✅ Found ICO icon file: {ico_path}")
    elif os.path.exists(png_path):
        icon_path = png_path
        print(f"✅ Found PNG icon file: {png_path}")
        print("💡 Tip: Run 'python convert_icon.py' to create an ICO file for better Windows support")
    else:
        print(f"❌ No icon file found. Looking for: {ico_path} or {png_path}")
        return False, None
    
    # Check file size (should be reasonable for an icon)
    file_size = os.path.getsize(icon_path)
    if file_size < 1000:  # Less than 1KB might be invalid
        print(f"⚠️  Icon file seems too small: {file_size} bytes")
        return False, None
    
    print(f"✅ Icon file verified: {icon_path} ({file_size:,} bytes)")
    return True, icon_path

def create_version_file():
    """Create a version file for Windows executable"""
    version_content = """# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(2,0,0,0),
    prodvers=(2,0,0,0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          u'040904B0',
          [StringStruct(u'CompanyName', u'Grace Biosensor'),
           StringStruct(u'FileDescription', u'Grace Biosensor Data Capture'),
           StringStruct(u'FileVersion', u'2.0.0.0'),
           StringStruct(u'InternalName', u'Grace-Biosensor-Capture'),
           StringStruct(u'LegalCopyright', u'MIT License'),
           StringStruct(u'OriginalFilename', u'Grace-Biosensor-Capture.exe'),
           StringStruct(u'ProductName', u'Grace Biosensor Data Capture'),
           StringStruct(u'ProductVersion', u'2.0.0.0')])
      ]
    ),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
"""
    
    with open('version.txt', 'w', encoding='utf-8') as f:
        f.write(version_content)
    
    print("✅ Version file created")

def build_executable(icon_path):
    """Build the executable using PyInstaller"""
    print("🔨 Building executable...")
    
    # Build command
    cmd = [
        'pyinstaller',
        '--clean',
        '--onefile',
        '--windowed',
        '--name=Grace-Biosensor-Capture',
        f'--icon={icon_path}',
        f'--add-data={icon_path};.',
        '--add-data=.env.example;.',
        '--add-data=config.py;.',
        '--add-data=README.md;.',
        '--add-data=LICENSE;.',
        '--hidden-import=PyQt5',
        '--hidden-import=requests',
        '--hidden-import=PIL',
        '--hidden-import=pyautogui',
        '--hidden-import=mss',
        '--hidden-import=pywinctl',
        '--hidden-import=numpy',
        '--hidden-import=psutil',
        '--hidden-import=pyperclip',
        '--hidden-import=qdarkstyle',
        '--hidden-import=qtawesome',
        '--hidden-import=pygments',
        '--hidden-import=rich',
        '--hidden-import=markdown',
        'main.py'
    ]
    
    # Add PNG file too if we're using ICO (as fallback)
    if icon_path.endswith('.ico') and os.path.exists('app_icon.png'):
        cmd.insert(-1, '--add-data=app_icon.png;.')
    
    print(f"📋 Using icon: {icon_path}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Build completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed with error:")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False

def main():
    """Main build process"""
    print("🚀 Grace Biosensor Capture - Build Process Starting...")
    print("=" * 60)
    
    # Step 1: Check requirements
    print("\n1. Checking requirements...")
    if not check_requirements():
        print("❌ Build aborted due to missing requirements")
        sys.exit(1)
    
    # Step 2: Verify icon file
    print("\n2. Verifying icon file...")
    icon_ok, icon_path = verify_icon_file()
    if not icon_ok:
        print("❌ Build aborted due to icon file issues")
        sys.exit(1)
    
    # Step 3: Clean build directories
    print("\n3. Cleaning build directories...")
    clean_build_directories()
    
    # Step 4: Create version file
    print("\n4. Creating version file...")
    create_version_file()
    
    # Step 5: Build executable
    print("\n5. Building executable...")
    if not build_executable(icon_path):
        print("❌ Build failed")
        sys.exit(1)
    
    # Step 6: Final verification
    print("\n6. Final verification...")
    exe_path = os.path.join('dist', 'Grace-Biosensor-Capture.exe')
    if os.path.exists(exe_path):
        file_size = os.path.getsize(exe_path)
        print(f"✅ Executable created: {exe_path}")
        print(f"📦 File size: {file_size:,} bytes ({file_size/1024/1024:.1f} MB)")
        
        # Create a shortcut info
        print("\n🎉 BUILD SUCCESSFUL!")
        print("=" * 60)
        print(f"📂 Executable location: {os.path.abspath(exe_path)}")
        print("🖱️  You can now run the application by double-clicking the .exe file")
        print("🎨 The application should now display your custom icon!")
        
    else:
        print("❌ Executable not found after build")
        sys.exit(1)

if __name__ == "__main__":
    main()
