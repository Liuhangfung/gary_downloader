# 🐧 Ubuntu Server Setup Guide

## Complete Step-by-Step Guide for Ubuntu/Linux Server

---

## 📋 Prerequisites

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip python3-venv -y

# Install FFmpeg (for audio extraction)
sudo apt install ffmpeg -y
```

---

## 🔧 Step 1: Setup Virtual Environment

```bash
# Navigate to project directory
cd /home/ken/AI/gary_downloader

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should now show (venv)
```

---

## 📦 Step 2: Install Dependencies

```bash
# Make sure venv is activated
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install yt-dlp (if not in requirements)
pip install yt-dlp

# Verify installation
python3 -c "import flask; import yt_dlp; print('✅ All packages installed!')"
```

---

## 🧪 Step 3: Test the Application

```bash
# Test development server first
python3 app.py

# Or test production server
python3 server.py

# Press Ctrl+C to stop
```

**Access from browser:**
- From server: `http://localhost:5000`
- From network: `http://192.168.10.177:5000`

---

## 🔥 Step 4: Create Systemd Service (Keep Running Forever)

### Create service file:

```bash
sudo nano /etc/systemd/system/gary_downloader.service
```

### Paste this configuration:

```ini
[Unit]
Description=GARY Downloader - Video Downloader Service
After=network.target

[Service]
Type=simple
User=ken
Group=ken
WorkingDirectory=/home/ken/AI/gary_downloader
Environment="PATH=/home/ken/AI/gary_downloader/venv/bin"
ExecStart=/home/ken/AI/gary_downloader/venv/bin/python3 /home/ken/AI/gary_downloader/server.py
Restart=always
RestartSec=10

# Logging
StandardOutput=append:/home/ken/AI/gary_downloader/gary_downloader.log
StandardError=append:/home/ken/AI/gary_downloader/gary_downloader_error.log

[Install]
WantedBy=multi-user.target
```

**Save:** Ctrl+O, Enter, Ctrl+X

---

## ⚙️ Step 5: Enable and Start Service

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable service (start on boot)
sudo systemctl enable gary_downloader

# Start service
sudo systemctl start gary_downloader

# Check status
sudo systemctl status gary_downloader
```

---

## 📊 Step 6: Manage the Service

### Start/Stop/Restart:
```bash
# Start
sudo systemctl start gary_downloader

# Stop
sudo systemctl stop gary_downloader

# Restart
sudo systemctl restart gary_downloader

# Status
sudo systemctl status gary_downloader
```

### View Logs:
```bash
# View live logs
sudo journalctl -u gary_downloader -f

# View last 100 lines
sudo journalctl -u gary_downloader -n 100

# View application logs
tail -f ~/AI/gary_downloader/gary_downloader.log

# View error logs
tail -f ~/AI/gary_downloader/gary_downloader_error.log
```

---

## 🌐 Step 7: Configure Firewall

```bash
# Check if UFW is active
sudo ufw status

# Allow port 5000
sudo ufw allow 5000/tcp

# Check again
sudo ufw status
```

---

## 🔐 Step 8: Setup Nginx Reverse Proxy (Optional but Recommended)

### Install Nginx:
```bash
sudo apt install nginx -y
```

### Create Nginx configuration:
```bash
sudo nano /etc/nginx/sites-available/gary_downloader
```

### Paste this:
```nginx
server {
    listen 80;
    server_name 192.168.10.177;  # or your domain

    client_max_body_size 2G;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket support
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        
        # Timeouts for large downloads
        proxy_connect_timeout 600;
        proxy_send_timeout 600;
        proxy_read_timeout 600;
        send_timeout 600;
    }
}
```

### Enable and restart Nginx:
```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/gary_downloader /etc/nginx/sites-enabled/

# Test configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
```

**Now access via:** `http://192.168.10.177` (no port needed!)

---

## 🎯 Quick Commands Reference

```bash
# Navigate to project
cd /home/ken/AI/gary_downloader

# Activate venv
source venv/bin/activate

# Update yt-dlp (do this regularly)
pip install --upgrade yt-dlp

# Restart service after updates
sudo systemctl restart gary_downloader

# Check if running
sudo systemctl status gary_downloader

# View live logs
sudo journalctl -u gary_downloader -f
```

---

## 🔄 Update Application

When you update code from GitHub:

```bash
# Navigate to project
cd /home/ken/AI/gary_downloader

# Pull latest changes
git pull origin main

# Activate venv
source venv/bin/activate

# Update dependencies (if requirements changed)
pip install -r requirements.txt

# Restart service
sudo systemctl restart gary_downloader

# Check status
sudo systemctl status gary_downloader
```

---

## 🛠️ Troubleshooting

### Service won't start:
```bash
# Check logs
sudo journalctl -u gary_downloader -n 50

# Check if port is in use
sudo netstat -tulpn | grep 5000

# Try running manually
cd /home/ken/AI/gary_downloader
source venv/bin/activate
python3 server.py
```

### Permission issues:
```bash
# Fix ownership
sudo chown -R ken:ken /home/ken/AI/gary_downloader

# Fix permissions
chmod +x /home/ken/AI/gary_downloader/server.py
```

### Can't access from network:
```bash
# Check firewall
sudo ufw status

# Check if service is listening
sudo netstat -tulpn | grep 5000

# Check Nginx (if using)
sudo systemctl status nginx
```

---

## 📈 Performance Tuning

### Increase threads in server.py:
```python
serve(app, host=host, port=port, threads=8)  # More concurrent downloads
```

### Automatic cleanup old downloads:
```bash
# Create cleanup script
nano ~/cleanup_downloads.sh
```

```bash
#!/bin/bash
# Delete downloads older than 7 days
find /home/ken/AI/gary_downloader/downloads -type f -mtime +7 -delete
```

```bash
# Make executable
chmod +x ~/cleanup_downloads.sh

# Add to crontab (run daily at 3 AM)
crontab -e
# Add line:
0 3 * * * /home/ken/cleanup_downloads.sh
```

---

## ✅ Verification Checklist

- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Application runs manually
- [ ] Systemd service created
- [ ] Service enabled and started
- [ ] Service status is active
- [ ] Can access from browser
- [ ] Firewall configured
- [ ] Nginx configured (optional)
- [ ] Logs are working

---

## 🎉 Done!

Your GARY_DOWNLOADER is now:
- ✅ Running 24/7
- ✅ Auto-starts on reboot
- ✅ Has proper logging
- ✅ Can handle multiple downloads
- ✅ Accessible from your network

**Access your downloader:**
- With Nginx: `http://192.168.10.177`
- Without Nginx: `http://192.168.10.177:5000`

**Enjoy! 🚀**

