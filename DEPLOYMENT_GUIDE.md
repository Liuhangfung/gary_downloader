# 🚀 GARY DOWNLOADER - Deployment Guide

## 📋 Table of Contents
1. [How It Works](#how-it-works)
2. [Local Server Deployment](#local-server-deployment)
3. [Production Setup](#production-setup)
4. [Network Access](#network-access)
5. [Troubleshooting](#troubleshooting)

---

## 🔧 How It Works

### Architecture Overview

```
User Browser (Web UI)
      ↓
Flask Web Server (app.py)
      ↓
yt-dlp Library
      ↓
Internet (Video Sources)
      ↓
Local Storage (downloads folder)
      ↓
User Downloads File to Computer
```

### Component Breakdown

#### 1. **Frontend (templates/index.html)**
- **Beautiful web interface** built with HTML, CSS, and JavaScript
- **Real-time progress tracking** using AJAX polling
- **User interactions**: Paste URL, select format, download
- Communicates with backend through REST API calls

#### 2. **Backend (app.py)**
- **Flask web server** handles all HTTP requests
- **API Endpoints**:
  - `/` - Serves the web UI
  - `/api/info` - Gets video information
  - `/api/download` - Starts video download
  - `/api/progress` - Returns download progress
  - `/api/downloads` - Lists downloaded files
  - `/api/download-file/<filename>` - Sends file to user's browser

#### 3. **yt-dlp Library**
- **Core downloader** that handles 1000+ video sites
- Extracts video information and metadata
- Downloads video/audio in various formats
- Progress tracking through hooks

#### 4. **Flow Example**

```
Step 1: User pastes URL and clicks "Get Info"
   → Frontend sends POST to /api/info with URL
   → Backend uses yt-dlp to extract video metadata
   → Returns: title, thumbnail, duration, available formats
   → Frontend displays this information

Step 2: User clicks "Download"
   → Frontend sends POST to /api/download with URL and settings
   → Backend starts download in background thread
   → yt-dlp downloads video to downloads/ folder
   → Progress hook updates download_progress dictionary

Step 3: Frontend polls /api/progress every 1 second
   → Backend returns current download percentage, speed, ETA
   → Frontend updates progress bar in real-time

Step 4: Download completes
   → File saved to downloads/ folder
   → Frontend refreshes file list automatically
   → Shows "Download" button next to file

Step 5: User clicks "Download" button on file
   → Browser requests /api/download-file/<filename>
   → Backend sends file using Flask's send_file()
   → Browser downloads file to user's computer
```

---

## 💻 Local Server Deployment

### Option 1: Quick Development Server (Current Setup)

**What you're running now:**

```bash
python app.py
```

**Pros:**
- ✅ Easy to start
- ✅ Auto-reloads on code changes
- ✅ Good for testing

**Cons:**
- ❌ Not for production use
- ❌ Single-threaded (one download at a time)
- ❌ No SSL/HTTPS

**Access:**
- Local: `http://localhost:5000`
- Network: `http://192.168.11.131:5000` (your local IP)

---

### Option 2: Production Server with Waitress (Recommended)

#### Step 1: Install Waitress

```bash
pip install waitress
```

#### Step 2: Create Production Server File

Create `server.py`:

```python
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
    host = '0.0.0.0'  # Listen on all interfaces
    port = 5000
    
    print("=" * 70)
    print("🚀 GARY_DOWNLOADER - Production Server")
    print("=" * 70)
    print(f"📱 Local access:   http://localhost:{port}")
    print(f"🌐 Network access: http://{get_local_ip()}:{port}")
    print("=" * 70)
    print("Press CTRL+C to stop the server")
    print("=" * 70)
    
    # Production-ready server
    serve(app, host=host, port=port, threads=4)
```

#### Step 3: Run Production Server

```bash
python server.py
```

**Features:**
- ✅ Production-ready WSGI server
- ✅ Multi-threaded (4 concurrent downloads)
- ✅ More stable and faster
- ✅ Better for multiple users

---

### Option 3: Run as Windows Service (Always Running)

#### Step 1: Install NSSM (Non-Sucking Service Manager)

Download from: https://nssm.cc/download

#### Step 2: Install Service

```powershell
# Open PowerShell as Administrator
cd "C:\path\to\nssm\win64"

# Install service
.\nssm.exe install GaryDownloader "C:\Users\USER\AppData\Local\Programs\Python\Python313\python.exe" "C:\Users\USER\Desktop\trading analysis\AI Project\GARY_DOWNLOADER\server.py"

# Start service
.\nssm.exe start GaryDownloader
```

#### Step 3: Manage Service

```powershell
# Check status
.\nssm.exe status GaryDownloader

# Stop service
.\nssm.exe stop GaryDownloader

# Remove service
.\nssm.exe remove GaryDownloader confirm
```

---

## 🌐 Network Access Setup

### Step 1: Find Your Server's IP Address

```powershell
# In PowerShell
ipconfig

# Look for "IPv4 Address" under your active network adapter
# Example: 192.168.1.100
```

### Step 2: Configure Windows Firewall

```powershell
# Run as Administrator
New-NetFirewallRule -DisplayName "GARY Downloader" -Direction Inbound -Protocol TCP -LocalPort 5000 -Action Allow
```

### Step 3: Access from Other Devices

From any device on your local network:

```
http://YOUR_SERVER_IP:5000

Example: http://192.168.1.100:5000
```

---

## 🔒 Production Setup Best Practices

### 1. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install waitress
```

### 2. Update requirements.txt

```bash
pip freeze > requirements.txt
```

### 3. Configure Environment Variables

Create `.env` file:

```
FLASK_ENV=production
DOWNLOAD_FOLDER=downloads
HOST=0.0.0.0
PORT=5000
```

### 4. Update app.py for Production

Add at the top of `app.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
DOWNLOAD_FOLDER = Path(os.getenv('DOWNLOAD_FOLDER', 'downloads'))
```

### 5. Set Download Location

You can change where files are saved by modifying `DOWNLOAD_FOLDER` in `app.py`:

```python
# Example: Save to a network drive
DOWNLOAD_FOLDER = Path('D:/Videos/Downloads')

# Or external drive
DOWNLOAD_FOLDER = Path('E:/Downloads')
```

---

## 🎯 Quick Start Commands

### For Development (Testing)
```bash
python app.py
```

### For Production (Local Server)
```bash
python server.py
```

### For Always-Running Service
```powershell
# Install and start (run as Admin)
.\nssm.exe install GaryDownloader [python_path] [server.py_path]
.\nssm.exe start GaryDownloader
```

---

## 📊 Monitoring and Logs

### View Logs in Real-Time

The server will print:
- Download progress
- API requests
- Errors and warnings

### Access Logs

Create a logging system in `app.py`:

```python
import logging

logging.basicConfig(
    filename='gary_downloader.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Log events
app.logger.info('Server started')
```

---

## 🛠️ Troubleshooting

### Issue: "Address already in use"

**Solution:** Change port in `server.py`:
```python
port = 8080  # Use different port
```

### Issue: Can't access from other devices

**Solutions:**
1. Check Windows Firewall settings
2. Ensure server is running with `host='0.0.0.0'`
3. Verify devices are on same network
4. Try server IP instead of hostname

### Issue: Download fails

**Solutions:**
1. Check internet connection
2. Verify video URL is valid
3. Some sites may require authentication
4. Try updating yt-dlp: `pip install --upgrade yt-dlp`

### Issue: Slow downloads

**Solutions:**
1. Check your internet speed
2. Server resources (CPU/RAM)
3. Close other applications
4. Try different video quality

---

## 📱 Mobile Access

Your phone/tablet can access the server too!

1. Connect to same WiFi network
2. Open browser
3. Go to: `http://YOUR_SERVER_IP:5000`
4. Works just like on desktop!

---

## 🔐 Security Recommendations

### For Local Network Only:
- ✅ Current setup is fine
- Keep firewall rule for port 5000

### For Internet Access (Advanced):
- ⚠️ Add authentication
- ⚠️ Use HTTPS/SSL
- ⚠️ Set up reverse proxy (nginx)
- ⚠️ Use VPN instead

---

## 📈 Performance Tips

1. **Increase threads** in `server.py`:
   ```python
   serve(app, host=host, port=port, threads=8)  # More concurrent downloads
   ```

2. **Use SSD** for download folder (faster writes)

3. **Allocate more RAM** if downloading many files

4. **Regular cleanup** of downloads folder

---

## 🎉 Summary

**You now have:**
- ✅ Working video downloader
- ✅ Beautiful web UI
- ✅ Real-time progress tracking
- ✅ Network access capability
- ✅ Production deployment option

**Next Steps:**
1. Choose deployment method (development vs production)
2. Set up network access if needed
3. Configure firewall
4. Share with others on your network!

**Enjoy your GARY DOWNLOADER! 🚀**

