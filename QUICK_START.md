# 🎯 GARY DOWNLOADER - Quick Start Guide

## 🚀 3 Ways to Run

### 1️⃣ Double-Click Method (Easiest)
```
Just double-click: START_SERVER.bat
```
✅ Automatically installs dependencies  
✅ Starts production server  
✅ Opens on: http://localhost:5000

---

### 2️⃣ Development Mode
```bash
python app.py
```
✅ Good for testing  
✅ Auto-reloads on changes  
⚠️ Single-threaded

---

### 3️⃣ Production Mode
```bash
python server.py
```
✅ Production-ready  
✅ Multi-threaded (4 concurrent downloads)  
✅ Better performance

---

## 📱 How to Access

### From Your Computer:
```
http://localhost:5000
```

### From Other Devices (Phone/Tablet/Other PCs):
```
http://YOUR_IP:5000

Example: http://192.168.11.131:5000
```

**Find your IP:**
```powershell
ipconfig
# Look for "IPv4 Address"
```

---

## 🎬 How to Use

### Step 1: Paste URL
- Copy any video URL (YouTube, TikTok, etc.)
- Paste into the input field

### Step 2: Get Info (Optional)
- Click "Get Info" to see video details
- View available formats and quality options

### Step 3: Choose Download Type
- **Video (Best Quality)** - Downloads best video
- **Audio Only (MP3)** - Extracts audio only
- **Custom Format** - Select specific quality after "Get Info"

### Step 4: Download
- Click "Download" button
- Watch real-time progress
- File appears in "Downloaded Files" section

### Step 5: Download to Computer
- Click "Download" button next to filename
- File downloads to your browser's download folder

---

## 🔥 Supported Sites

✅ YouTube  
✅ TikTok  
✅ Instagram  
✅ Twitter/X  
✅ Facebook  
✅ Vimeo  
✅ Twitch  
✅ Reddit  
✅ 1000+ more sites!

---

## ⚙️ Firewall Setup (For Network Access)

### Open Windows Firewall:
```powershell
# Run PowerShell as Administrator
New-NetFirewallRule -DisplayName "GARY Downloader" -Direction Inbound -Protocol TCP -LocalPort 5000 -Action Allow
```

Now other devices can access your server!

---

## 📁 File Locations

**Downloaded videos:** `downloads/` folder  
**Logs:** Console output  
**Settings:** `app.py` file

---

## 🛠️ Troubleshooting

### Can't access from other devices?
1. Check firewall (see above)
2. Make sure you're on the same WiFi
3. Use server IP address, not "localhost"

### Port already in use?
Edit `server.py` and change:
```python
port = 8080  # Use different port
```

### Download fails?
- Check internet connection
- Try updating: `pip install --upgrade yt-dlp`
- Some videos may be region-restricted

---

## 💡 Pro Tips

1. **Get Info First** - See all quality options before downloading
2. **Select Custom Format** - Click on format after "Get Info" for specific quality
3. **Mobile Friendly** - Works perfectly on phones and tablets
4. **Batch Downloads** - Start multiple downloads (with production server)
5. **Keyboard Shortcuts** - Ctrl+V to paste, Enter to start download

---

## 🎉 You're Ready!

**Start server:** Double-click `START_SERVER.bat`  
**Open browser:** Go to http://localhost:5000  
**Download videos:** Paste URL → Download → Enjoy!

---

## 📞 Need Help?

Check the full guide: `DEPLOYMENT_GUIDE.md`

**Happy Downloading! 🚀**

