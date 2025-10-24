#!/usr/bin/env python3
"""
Direct downloader script - Download files reliably from GARY_DOWNLOADER server
Run this on your Windows PC to download videos without browser issues
"""

import requests
import sys
import os
from pathlib import Path

# Configuration
SERVER_URL = "http://192.168.10.177:5000"
DOWNLOAD_FOLDER = Path.home() / "Downloads" / "gary_videos"

def get_available_files():
    """Get list of files from server"""
    try:
        response = requests.get(f"{SERVER_URL}/api/downloads")
        data = response.json()
        return data.get('files', [])
    except Exception as e:
        print(f"❌ Error getting file list: {e}")
        return []

def download_file(filename, output_dir):
    """Download a file from server with progress"""
    try:
        url = f"{SERVER_URL}/api/download-file/{filename}"
        print(f"📥 Downloading: {filename}")
        
        # Stream download with progress
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Get file size
        total_size = int(response.headers.get('content-length', 0))
        
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / filename
        
        # Download with progress
        downloaded = 0
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        progress = (downloaded / total_size) * 100
                        print(f"\r⏳ Progress: {progress:.1f}% ({downloaded}/{total_size} bytes)", end='')
        
        print(f"\n✅ Downloaded successfully: {output_path}")
        return True
        
    except Exception as e:
        print(f"\n❌ Error downloading {filename}: {e}")
        return False

def main():
    """Main function"""
    print("=" * 70)
    print("🎬 GARY DOWNLOADER - Direct Download Script")
    print("=" * 70)
    print(f"📡 Server: {SERVER_URL}")
    print(f"💾 Download to: {DOWNLOAD_FOLDER}")
    print("=" * 70)
    
    # Get available files
    print("\n🔍 Fetching available files...")
    files = get_available_files()
    
    if not files:
        print("❌ No files found or server is not accessible")
        return
    
    # Display files
    print(f"\n📂 Available files ({len(files)}):\n")
    for i, file in enumerate(files, 1):
        print(f"  {i}. {file['name']} ({file['size']})")
    
    # Download selection
    print("\n" + "=" * 70)
    choice = input("\nEnter file number to download (or 'all' for all files): ").strip()
    
    if choice.lower() == 'all':
        print(f"\n📥 Downloading all {len(files)} files...\n")
        success_count = 0
        for file in files:
            if download_file(file['name'], DOWNLOAD_FOLDER):
                success_count += 1
            print()
        
        print("=" * 70)
        print(f"✅ Downloaded {success_count}/{len(files)} files successfully")
        print(f"📂 Files saved to: {DOWNLOAD_FOLDER}")
        
    else:
        try:
            index = int(choice) - 1
            if 0 <= index < len(files):
                file = files[index]
                download_file(file['name'], DOWNLOAD_FOLDER)
                print("\n" + "=" * 70)
                print(f"📂 File saved to: {DOWNLOAD_FOLDER}")
            else:
                print("❌ Invalid file number")
        except ValueError:
            print("❌ Please enter a valid number or 'all'")
    
    print("\n✨ Done!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Download cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")

