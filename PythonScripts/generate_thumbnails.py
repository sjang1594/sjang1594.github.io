#!/usr/bin/env python3
"""
Generate optimized thumbnails for photo gallery
Requires: Pillow (pip install Pillow)
"""

from PIL import Image
import os
from pathlib import Path

# Configuration
SOURCE_DIR = Path("assets/img/photo/film-photo")
THUMB_DIR = SOURCE_DIR / "thumbnails"
MAX_SIZE = 800  # Max width/height for thumbnails
QUALITY = 85    # JPEG quality (0-100)

def create_thumbnail(input_path, output_path, max_size=MAX_SIZE, quality=QUALITY):
    """Create an optimized thumbnail from an image"""
    try:
        with Image.open(input_path) as img:
            # Convert RGBA to RGB if necessary
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background

            # Calculate new size maintaining aspect ratio
            img.thumbnail((max_size, max_size), Image.LANCZOS)

            # Save optimized version
            img.save(output_path, 'JPEG', quality=quality, optimize=True)

            # Get file sizes
            original_size = input_path.stat().st_size / 1024 / 1024  # MB
            new_size = output_path.stat().st_size / 1024 / 1024      # MB
            reduction = ((original_size - new_size) / original_size) * 100

            print(f"[OK] {input_path.name}")
            print(f"  {original_size:.2f}MB -> {new_size:.2f}MB ({reduction:.1f}% reduction)")

    except Exception as e:
        print(f"[ERROR] Error processing {input_path.name}: {e}")

def main():
    # Create thumbnails directory if it doesn't exist
    THUMB_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Generating thumbnails...")
    print(f"Source: {SOURCE_DIR}")
    print(f"Output: {THUMB_DIR}")
    print(f"Max size: {MAX_SIZE}px")
    print(f"Quality: {QUALITY}%")
    print("-" * 50)

    # Process all images
    image_extensions = {'.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG'}
    processed = 0
    total_original = 0
    total_compressed = 0

    for file_path in SOURCE_DIR.iterdir():
        if file_path.suffix in image_extensions and file_path.is_file():
            output_path = THUMB_DIR / file_path.name

            # Track sizes
            original_size = file_path.stat().st_size / 1024 / 1024
            total_original += original_size

            create_thumbnail(file_path, output_path)

            compressed_size = output_path.stat().st_size / 1024 / 1024
            total_compressed += compressed_size

            processed += 1

    print("-" * 50)
    print(f"\nSummary:")
    print(f"  Images processed: {processed}")
    print(f"  Total original size: {total_original:.2f}MB")
    print(f"  Total compressed size: {total_compressed:.2f}MB")
    print(f"  Total saved: {total_original - total_compressed:.2f}MB")
    print(f"  Overall reduction: {((total_original - total_compressed) / total_original * 100):.1f}%")
    print(f"\n[SUCCESS] Thumbnails generated successfully!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\n[ERROR] Error: {e}")
