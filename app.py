from flask import Flask, render_template, request, jsonify, send_file
import yt_dlp
import os
import json
from pathlib import Path
import threading
import time

app = Flask(__name__)

# Configuration
DOWNLOAD_FOLDER = Path('downloads')
DOWNLOAD_FOLDER.mkdir(exist_ok=True)
CLEANUP_INTERVAL = 300  # 5 minutes in seconds
FILE_MAX_AGE = 300  # Delete files older than 5 minutes

# Store download progress
download_progress = {}

def progress_hook(d):
    """Hook to track download progress"""
    if d['status'] == 'downloading':
        downloaded = d.get('downloaded_bytes', 0)
        total = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
        if total > 0:
            percentage = (downloaded / total) * 100
            speed = d.get('speed', 0)
            eta = d.get('eta', 0)
            
            download_progress[d.get('info_dict', {}).get('id', 'unknown')] = {
                'percentage': round(percentage, 1),
                'downloaded': format_bytes(downloaded),
                'total': format_bytes(total),
                'speed': format_bytes(speed) + '/s' if speed else 'N/A',
                'eta': f"{eta}s" if eta else 'N/A',
                'status': 'downloading'
            }
    elif d['status'] == 'finished':
        download_progress[d.get('info_dict', {}).get('id', 'unknown')] = {
            'percentage': 100,
            'status': 'finished'
        }

def format_bytes(bytes_value):
    """Convert bytes to human readable format"""
    if not bytes_value:
        return '0 B'
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f} TB"

def cleanup_old_files():
    """Delete files older than FILE_MAX_AGE seconds"""
    try:
        current_time = time.time()
        deleted_count = 0
        
        for file in DOWNLOAD_FOLDER.iterdir():
            if file.is_file() and not file.name.startswith('.'):
                # Get file age
                file_age = current_time - file.stat().st_mtime
                
                # Delete if older than max age
                if file_age > FILE_MAX_AGE:
                    try:
                        file.unlink()
                        deleted_count += 1
                        print(f"🗑️  Deleted old file: {file.name} (age: {int(file_age/60)} minutes)")
                    except Exception as e:
                        print(f"❌ Error deleting {file.name}: {e}")
        
        if deleted_count > 0:
            print(f"✅ Cleanup complete: {deleted_count} file(s) deleted")
        
    except Exception as e:
        print(f"❌ Cleanup error: {e}")

def cleanup_scheduler():
    """Run cleanup every CLEANUP_INTERVAL seconds"""
    while True:
        time.sleep(CLEANUP_INTERVAL)
        cleanup_old_files()

# Start cleanup thread
cleanup_thread = threading.Thread(target=cleanup_scheduler, daemon=True)
cleanup_thread.start()
print(f"🧹 Auto-cleanup enabled: Files will be deleted after {FILE_MAX_AGE//60} minutes")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/info', methods=['POST'])
def get_info():
    """Get video information without downloading"""
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({'error': 'No URL provided'}), 400
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Extract formats
            formats = []
            if 'formats' in info:
                for f in info['formats']:
                    format_info = {
                        'format_id': f.get('format_id'),
                        'ext': f.get('ext'),
                        'resolution': f.get('resolution', 'audio only' if f.get('vcodec') == 'none' else 'N/A'),
                        'filesize': format_bytes(f.get('filesize', 0)),
                        'vcodec': f.get('vcodec', 'none'),
                        'acodec': f.get('acodec', 'none'),
                    }
                    formats.append(format_info)
            
            return jsonify({
                'success': True,
                'info': {
                    'title': info.get('title'),
                    'duration': info.get('duration'),
                    'uploader': info.get('uploader'),
                    'view_count': info.get('view_count'),
                    'thumbnail': info.get('thumbnail'),
                    'description': info.get('description', '')[:500],
                    'formats': formats
                }
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download', methods=['POST'])
def download():
    """Download video"""
    try:
        data = request.json
        url = data.get('url')
        download_type = data.get('type', 'video')  # video, audio, custom
        format_id = data.get('format_id')
        
        if not url:
            return jsonify({'error': 'No URL provided'}), 400
        
        ydl_opts = {
            'outtmpl': str(DOWNLOAD_FOLDER / '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook],
        }
        
        if download_type == 'audio':
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        elif download_type == 'custom' and format_id:
            ydl_opts['format'] = format_id
        else:
            ydl_opts['format'] = 'best'
        
        def download_video():
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    download_progress[info.get('id', 'unknown')] = {
                        'percentage': 100,
                        'status': 'completed',
                        'filename': info.get('title', 'Unknown')
                    }
            except Exception as e:
                download_progress['error'] = str(e)
        
        # Start download in background thread
        thread = threading.Thread(target=download_video)
        thread.start()
        
        return jsonify({
            'success': True,
            'message': 'Download started'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/progress', methods=['GET'])
def get_progress():
    """Get download progress"""
    return jsonify(download_progress)

@app.route('/api/downloads', methods=['GET'])
def list_downloads():
    """List downloaded files"""
    try:
        files = []
        for file in DOWNLOAD_FOLDER.iterdir():
            if file.is_file():
                files.append({
                    'name': file.name,
                    'size': format_bytes(file.stat().st_size),
                    'path': str(file)
                })
        return jsonify({'files': files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download-file/<path:filename>', methods=['GET'])
def download_file(filename):
    """Download a specific file to user's computer"""
    try:
        from urllib.parse import unquote
        from flask import Response
        
        # Decode URL-encoded filename
        decoded_filename = unquote(filename)
        file_path = DOWNLOAD_FOLDER / decoded_filename
        
        if file_path.exists() and file_path.is_file():
            # Get file size
            file_size = file_path.stat().st_size
            
            # Use send_file with proper settings for large files
            return send_file(
                file_path,
                as_attachment=True,
                download_name=decoded_filename,
                mimetype='video/mp4',
                conditional=True,
                etag=True,
                last_modified=file_path.stat().st_mtime,
                max_age=0
            )
        else:
            # Debug: list available files
            available_files = [f.name for f in DOWNLOAD_FOLDER.iterdir() if f.is_file()]
            return jsonify({
                'error': 'File not found',
                'requested': decoded_filename,
                'available_files': available_files
            }), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 GARY_DOWNLOADER - Web UI")
    print("=" * 60)
    print("📱 Open your browser and go to: http://localhost:5000")
    print("💾 Downloads will be saved to:", DOWNLOAD_FOLDER.absolute())
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)

