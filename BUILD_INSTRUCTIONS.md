# 🔨 Building GARY DOWNLOADER Standalone Executable

This guide shows you how to create a standalone `.exe` file that users can download and run without any setup!

---

## 📋 Prerequisites

1. **Python installed** on your Windows PC
2. **All dependencies installed**

---

## 🚀 Quick Build (3 Steps)

### Step 1: Install PyInstaller

```powershell
pip install pyinstaller
```

### Step 2: Run Build Script

```powershell
python build_exe.py
```

### Step 3: Find Your Executable

The `.exe` file will be in:
```
dist\GaryDownloader.exe
```

That's it! 🎉

---

## 📦 Distribution

### What to Give Users:

**Option A: Single File (Simplest)**
- Just give them: `GaryDownloader.exe`
- They double-click it and it works!
- Downloads folder created automatically

**Option B: Folder with FFmpeg (Recommended)**
```
GaryDownloader/
├── GaryDownloader.exe
├── ffmpeg.exe          (optional, for audio extraction)
└── README.txt         (simple usage instructions)
```

---

## 🎯 How Users Use It

### For Users (No Technical Knowledge Required):

1. **Download** `GaryDownloader.exe`
2. **Double-click** to run
3. **Browser opens automatically** with the downloader
4. **Paste video URL** and download!
5. **Files save** to `downloads` folder next to the .exe

That's all they need to do! 🎬

---

## ⚙️ Advanced Build Options

### Build with Console Window (for debugging):

```powershell
# Edit build_exe.py and remove the --windowed flag
# Then run:
python build_exe.py
```

### Build with Custom Icon:

```powershell
# Create an icon file: icon.ico
# Edit build_exe.py and change:
# '--icon=NONE'  to  '--icon=icon.ico'
```

### Include FFmpeg in the Build:

```powershell
# Download ffmpeg.exe
# Copy it to the project folder
# Edit build_exe.py and add:
# '--add-binary=ffmpeg.exe;.'
```

---

## 🔍 Testing the Executable

### Test Locally:

```powershell
# Navigate to dist folder
cd dist

# Run the executable
.\GaryDownloader.exe
```

### What Should Happen:

1. ✅ Console window appears (if not using --windowed)
2. ✅ Browser opens automatically to http://localhost:5000
3. ✅ Web interface loads
4. ✅ Can download videos
5. ✅ Videos save to `downloads` folder

---

## 📊 File Sizes

Expect these sizes:
- **GaryDownloader.exe**: ~50-100 MB (includes Python + all libraries)
- With FFmpeg: ~150-200 MB

---

## 🎁 Creating a Release Package

### Professional Distribution:

```
GaryDownloader-v1.0/
├── GaryDownloader.exe
├── README.txt
├── LICENSE.txt
└── ffmpeg.exe (optional)
```

### README.txt for Users:

```
GARY DOWNLOADER
===============

HOW TO USE:
1. Double-click GaryDownloader.exe
2. Browser will open automatically
3. Paste video URL and click Download
4. Videos save to "downloads" folder

SUPPORTED SITES:
- YouTube, TikTok, Instagram, Twitter, Facebook
- And 1000+ more websites!

NEED HELP?
- Visit: https://github.com/Liuhangfung/gary_downloader
```

---

## 🐛 Troubleshooting Build Issues

### Issue: "PyInstaller not found"
```powershell
pip install pyinstaller
```

### Issue: "Module not found during build"
```powershell
# Install missing modules
pip install -r requirements.txt
pip install pyinstaller
```

### Issue: ".exe is too large"
- This is normal! It includes Python + all libraries
- You can use `--onedir` instead of `--onefile` for faster startup

### Issue: "ffmpeg not found in .exe"
- Users will get a warning but videos will still download
- For audio extraction, include ffmpeg.exe separately

---

## 🔄 Updating the Executable

When you update the code:

```powershell
# 1. Pull latest changes
git pull origin main

# 2. Rebuild
python build_exe.py

# 3. New .exe is in dist/
```

---

## 🌐 Alternative: Build for Different Platforms

### Windows (your current platform):
```powershell
python build_exe.py
```

### Linux/Mac Users Can Build Too:
```bash
# On Linux
python build_exe.py  # Creates a Linux binary

# On Mac
python build_exe.py  # Creates a Mac app
```

---

## 📤 Sharing Your Executable

### Upload Options:

1. **GitHub Releases** - Create a release on your repository
2. **Google Drive / Dropbox** - Share download link
3. **Your Website** - Direct download
4. **WeTransfer** - For large files

### Example Release:

```
GaryDownloader-Windows-v1.0.zip (180 MB)
├── GaryDownloader.exe
├── README.txt
└── ffmpeg.exe
```

---

## ✅ Checklist Before Release

- [ ] Test .exe on a clean Windows machine
- [ ] Verify browser auto-opens
- [ ] Test downloading a video
- [ ] Check downloads folder is created
- [ ] Include README.txt with instructions
- [ ] Test with and without internet connection
- [ ] Verify file sizes are reasonable
- [ ] Create virus scan report (optional, for user trust)

---

## 🎉 You're Done!

Users can now just:
1. Download your .exe
2. Run it
3. Download videos!

No Python, no setup, no configuration needed! 🚀

