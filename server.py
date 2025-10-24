#!/usr/bin/env python3
"""
GARY_DOWNLOADER - Production Server
Uses Waitress for production-ready WSGI server
"""

try:
    from waitress import serve
except ImportError:
    print("❌ Waitress is not installed!")
    print("📦 Installing waitress...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'waitress'])
    from waitress import serve

from app import app
import socket


def get_local_ip():
    """Get local network IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "localhost"


if __name__ == '__main__':
    # Server configuration
    host = '0.0.0.0'  # Listen on all network interfaces
    port = 5000       # Port number
    threads = 4       # Number of threads (concurrent downloads)
    
    local_ip = get_local_ip()
    
    print("=" * 70)
    print("🚀 GARY_DOWNLOADER - Production Server")
    print("=" * 70)
    print(f"📱 Local access:   http://localhost:{port}")
    print(f"🌐 Network access: http://{local_ip}:{port}")
    print("=" * 70)
    print(f"⚙️  Server config: {threads} threads, listening on {host}:{port}")
    print("💾 Downloads folder: downloads/")
    print("=" * 70)
    print("✨ Server is running! Press CTRL+C to stop")
    print("=" * 70)
    print()
    
    # Start production server
    try:
        serve(
            app, 
            host=host, 
            port=port, 
            threads=threads,
            url_scheme='http'
        )
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Try running: python app.py (for development mode)")

