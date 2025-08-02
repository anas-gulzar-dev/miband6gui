#!/usr/bin/env python3
"""
Icon Converter for Grace Biosensor Capture
Converts app_icon.png to app_icon.ico for better Windows taskbar support
"""

import os
import sys
from PIL import Image

def convert_png_to_ico(png_path="app_icon.png", ico_path="app_icon.ico"):
    """
    Convert PNG icon to ICO format for better Windows compatibility
    
    Args:
        png_path (str): Path to the PNG icon file
        ico_path (str): Path for the output ICO file
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Check if PNG file exists
        if not os.path.exists(png_path):
            print(f"❌ PNG file not found: {png_path}")
            return False
        
        # Open the PNG image
        with Image.open(png_path) as img:
            print(f"📷 Original image: {img.size[0]}x{img.size[1]} pixels")
            
            # Convert to RGBA if not already
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Create multiple sizes for ICO file (Windows standard sizes)
            sizes = [
                (16, 16),    # Small icon
                (32, 32),    # Medium icon  
                (48, 48),    # Large icon
                (64, 64),    # Extra large icon
                (128, 128),  # Jumbo icon
                (256, 256)   # Ultra large icon
            ]
            
            # Create list of resized images
            ico_images = []
            for size in sizes:
                resized = img.resize(size, Image.Resampling.LANCZOS)
                ico_images.append(resized)
                print(f"✅ Created {size[0]}x{size[1]} version")
            
            # Save as ICO file with multiple sizes
            ico_images[0].save(
                ico_path,
                format='ICO',
                sizes=[(img.size[0], img.size[1]) for img in ico_images],
                append_images=ico_images[1:]
            )
            
            print(f"✅ ICO file created successfully: {ico_path}")
            
            # Check file size
            file_size = os.path.getsize(ico_path)
            print(f"📦 ICO file size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
            
            return True
            
    except Exception as e:
        print(f"❌ Error converting PNG to ICO: {str(e)}")
        return False

def main():
    """Main function to convert icon"""
    print("🎨 Grace Biosensor - Icon Converter")
    print("=" * 50)
    
    # Check if PIL is available
    try:
        from PIL import Image
        print("✅ PIL (Pillow) is available")
    except ImportError:
        print("❌ PIL (Pillow) is not installed")
        print("Please install it with: pip install Pillow")
        sys.exit(1)
    
    # Convert the icon
    if convert_png_to_ico():
        print("\n🎉 Conversion successful!")
        print("Your app_icon.ico file is ready for better Windows taskbar support.")
        print("The build script will automatically use this ICO file if available.")
    else:
        print("\n❌ Conversion failed!")
        print("Please ensure app_icon.png exists and is a valid PNG file.")
        sys.exit(1)

if __name__ == "__main__":
    main()
