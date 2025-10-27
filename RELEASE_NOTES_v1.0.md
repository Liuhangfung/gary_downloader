# 🎬 GARY DOWNLOADER v1.0

**The easiest way to download videos from YouTube and 1000+ websites!**

---

## ✨ Features

✅ **Download from 1000+ websites** - YouTube, Facebook, Twitter, TikTok, Instagram, and more!  
✅ **Video or Audio** - Download full videos or extract audio as MP3  
✅ **Multiple Quality Options** - Choose your preferred quality  
✅ **Beautiful Web Interface** - Clean, modern, easy to use  
✅ **Real-time Progress** - See download progress in real-time  
✅ **One-Click Shutdown** - Red button in top-right to stop the app  
✅ **Automatic Cleanup** - Old downloads deleted after 5 minutes  
✅ **NO SETUP REQUIRED** - Just download and run!

---

## 🚀 How to Use

### For Regular Users (Super Easy!)

1. **Download** `GaryDownloader.exe` from this release
2. **Double-click** to run
3. **Browser opens automatically** to http://localhost:5000
4. **Paste video URL** and click Download!
5. **Click the red "Shut Down" button** when done

**That's it!** No Python, no installation, no hassle! 🎉

---

## 💻 System Requirements

- **Windows 7/8/10/11** (64-bit)
- **Internet connection** (for downloading videos)
- **~100MB free disk space** (for the app)

---

## ⚠️ First Run Warning

When you first run `GaryDownloader.exe`, Windows might show:
```
"Windows protected your PC"
```

**This is normal!** Click **"More info"** → **"Run anyway"**

This happens because the app is not digitally signed (costs $$$). The app is completely safe!

---

## 🎥 Supported Websites

YouTube, Facebook, Twitter/X, TikTok, Instagram, Vimeo, Dailymotion, Reddit, and **1000+ more!**

Full list: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

---

## 📖 Tips

- **Use VLC Media Player** for best video compatibility
- **Downloads auto-delete** after 5 minutes (to save space)
- **Port 5000** is used - close other apps using this port
- **Click red button** in top-right to shut down the app

---

## 🐛 Troubleshooting

**"Address already in use"**  
→ Something else is using port 5000. Close other programs or restart your PC.

**Download hangs at 98%**  
→ Wait 10-15 seconds - it's finalizing the file.

**Video won't play**  
→ Use VLC Media Player (it handles all formats).

---

## 👨‍💻 For Developers

Want to run from source code?

```bash
git clone https://github.com/Liuhangfung/gary_downloader.git
cd gary_downloader
pip install -r requirements.txt
python gary_downloader_gui.py
```

---

## 📜 License

Free to use for personal and educational purposes.

Built with: Python, Flask, yt-dlp, PyInstaller

---

## 💬 Feedback

Found a bug? Have a suggestion? Open an issue!

---

**Enjoy downloading! 🎬✨**

