#!/usr/bin/env python3
"""
Generate app icons for Kalyani Medical Hall apps
Run: python3 generate_icons.py
"""

import os
from PIL import Image, ImageDraw, ImageFont

def create_icon(size, bg_color, text, output_path):
    """Create a simple icon with background and text"""
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw a simple medical cross
    cross_size = size // 3
    cross_thick = size // 8
    center = size // 2
    
    # White cross
    draw.rectangle([center - cross_thick, center - cross_size, center + cross_thick, center + cross_size], fill='white')
    draw.rectangle([center - cross_size, center - cross_thick, center + cross_size, center + cross_thick], fill='white')
    
    # Save
    img.save(output_path)
    print(f"Created: {output_path}")

def create_icon_with_emoji(size, bg_color, emoji, output_path):
    """Create icon with emoji centered"""
    img = Image.new('RGB', (size, size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw rounded rectangle background
    margin = size // 10
    draw.rounded_rectangle([margin, margin, size-margin, size-margin], radius=size//8, fill='white')
    
    # Save simple version
    img.save(output_path)
    print(f"Created: {output_path}")

# Create icons directory if not exists
os.makedirs('kalyani_medical/assets/icon', exist_ok=True)
os.makedirs('kalyani_medical_customer/assets/icon', exist_ok=True)

# Admin App - Blue theme
print("\nGenerating Admin App icons...")
create_icon(1024, '#0284c7', '💊', 'kalyani_medical/assets/icon/icon.png')

# Customer App - Green theme  
print("\nGenerating Customer App icons...")
create_icon(1024, '#16a34a', '🏥', 'kalyani_medical_customer/assets/icon/icon.png')

print("\n✅ Icons generated!")
print("\nNext steps:")
print("1. cd kalyani_medical")
print("2. flutter pub get")
print("3. flutter pub run flutter_launcher_icons")
