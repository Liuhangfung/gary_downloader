#!/usr/bin/env python3
"""
Build script for creating Windows executable
Run this to create the standalone .exe
"""

import PyInstaller.__main__
import shutil
from pathlib import Path

def build():
    """Build the executable"""
    print("🔨 Building GARY DOWNLOADER executable...")
    print()
    
    # PyInstaller arguments
    PyInstaller.__main__.run([
        'gary_downloader_gui.py',           # Main script
        '--name=GaryDownloader',            # Output name
        '--onefile',                        # Single executable
        '--windowed',                       # No console window (optional)
        '--icon=NONE',                      # Add icon if you have one
        '--add-data=templates;templates',   # Include templates folder
        '--hidden-import=yt_dlp',          # Include yt-dlp
        '--hidden-import=flask',           # Include flask
        '--hidden-import=waitress',        # Include waitress
        '--collect-all=yt_dlp',           # Collect all yt-dlp files
        '--clean',                         # Clean before build
    ])
    
    print()
    print("=" * 70)
    print("✅ Build complete!")
    print("=" * 70)
    print()
    print("📂 Your executable is in: dist/GaryDownloader.exe")
    print()
    print("📦 Distribution package includes:")
    print("   - GaryDownloader.exe")
    print("   - Downloads will be created automatically")
    print()
    print("🎉 Users can now just run GaryDownloader.exe!")

if __name__ == "__main__":
    try:
        build()
    except Exception as e:
        print(f"❌ Build failed: {e}")
        print()
        print("💡 Make sure PyInstaller is installed:")
        print("   pip install pyinstaller")

