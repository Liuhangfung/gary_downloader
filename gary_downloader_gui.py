#!/usr/bin/env python3
"""
GARY DOWNLOADER - Standalone Launcher
Auto-opens browser and starts server
"""

import sys
import webbrowser
import threading
import time
from pathlib import Path

# Import the Flask app
from app import app, DOWNLOAD_FOLDER

def open_browser():
    """Open browser after a short delay"""
    time.sleep(2)
    webbrowser.open('http://localhost:5000')

def main():
    """Main launcher function"""
    print("=" * 70)
    print("🎬 GARY DOWNLOADER - Starting...")
    print("=" * 70)
    print()
    print("📂 Downloads will be saved to:", DOWNLOAD_FOLDER.absolute())
    print("🌐 Opening web browser...")
    print()
    print("💡 To stop: Close this window or press Ctrl+C")
    print("=" * 70)
    print()
    
    # Open browser in background thread
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Start Flask app
    try:
        app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print("\n\n👋 GARY DOWNLOADER stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()

