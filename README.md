# 🎬 GARY DOWNLOADER

A beautiful web-based video downloader powered by yt-dlp with a modern UI.

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-Unlicense-green.svg)

---

## 📥 **Download for Windows (Easy Way!)**

### **👉 [Download GaryDownloader.exe](https://github.com/Liuhangfung/gary_downloader/releases) 👈**

**No Python? No problem!** Just download, double-click, and start downloading videos!

✅ No installation required  
✅ No Python needed  
✅ Just run and go!

---

## 🚀 Quick Start (For Developers)

### Easiest Way: Double-Click to Start!
```
📁 Double-click: START_SERVER.bat
```

### Or run manually:
```bash
# Development mode
python app.py

# Production mode (recommended)
python server.py
```

### Open browser:
```
http://localhost:5000
```

### Access from other devices:
```
http://YOUR_LOCAL_IP:5000
```

## 📖 Documentation

- **Quick Start Guide**: [QUICK_START.md](QUICK_START.md) - Get started in 2 minutes!
- **Full Deployment Guide**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Complete setup & architecture

## 🎯 How It Works (Simple)

```
┌─────────────────┐
│   Your Browser  │  ← Beautiful Web UI
└────────┬────────┘
         │
    ┌────▼─────┐
    │  Flask   │  ← Web Server
    │  Server  │
    └────┬─────┘
         │
    ┌────▼─────┐
    │  yt-dlp  │  ← Video Downloader
    └────┬─────┘
         │
    ┌────▼─────┐
    │ Internet │  ← 1000+ Video Sites
    └────┬─────┘
         │
    ┌────▼─────┐
    │downloads/│  ← Your Videos
    └──────────┘
         │
    ┌────▼─────┐
    │   Your   │  ← Download to Computer
    │ Computer │
    └──────────┘
```

## ✨ Features

- 🎨 **Beautiful Modern UI** - Clean and intuitive interface
- 📥 **Multiple Download Options**:
  - Best quality video
  - Audio only (MP3)
  - Custom format selection
- 📊 **Real-time Progress** - Watch your downloads in real-time
- ℹ️ **Video Info** - Preview video details before downloading
- 📂 **Download Manager** - See all your downloaded files
- 🌐 **1000+ Supported Sites** - YouTube, TikTok, Instagram, Twitter, Vimeo, and more!

## 📋 Requirements

- Python 3.7+
- Flask
- yt-dlp

Install dependencies:
```bash
pip install -r requirements.txt
```

## 💡 Usage Tips

1. **Get Video Info First**: Click "Get Info" to see available formats and quality options
2. **Select Custom Format**: After getting info, you can click on any format to select it specifically
3. **Audio Downloads**: Select "Audio Only (MP3)" to extract just the audio (requires FFmpeg)
4. **Downloads Location**: All files are saved to the `downloads/` folder

## 🛠️ Optional: FFmpeg Installation

For audio extraction and format conversion, install FFmpeg:

- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
- **Mac**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

## 📂 Project Structure

```
GARY_DOWNLOADER/
├── 📄 START_SERVER.bat      # Double-click to start (Windows)
├── 🐍 app.py                # Flask backend (development)
├── 🐍 server.py             # Production server (Waitress)
├── 📁 templates/
│   └── 🎨 index.html        # Beautiful Web UI
├── 📁 downloads/            # Downloaded videos (auto-created)
├── 📁 yt-dlp/               # yt-dlp source code
├── 📋 requirements.txt      # Python dependencies
├── 📖 README.md             # This file
├── 📖 QUICK_START.md        # Quick start guide
├── 📖 DEPLOYMENT_GUIDE.md   # Full deployment guide
└── 🔧 .gitignore            # Git ignore file
```

## 🎯 Supported Sites

yt-dlp supports over 1000 websites including:
- YouTube
- TikTok
- Instagram
- Twitter/X
- Facebook
- Vimeo
- Twitch
- Reddit
- And many more!

[See full list](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## 🔧 Advanced Usage

### API Endpoints

- `GET /` - Web UI
- `POST /api/info` - Get video information
- `POST /api/download` - Start download
- `GET /api/progress` - Get download progress
- `GET /api/downloads` - List downloaded files

### Example API Call

```bash
curl -X POST http://localhost:5000/api/info \
  -H "Content-Type: application/json" \
  -d '{"url":"YOUR_VIDEO_URL"}'
```

## 📝 License

This project uses yt-dlp which is licensed under the Unlicense.

## 🙏 Credits

Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp) - A youtube-dl fork with additional features and fixes.

---

Made with ❤️ for easy video downloading!
