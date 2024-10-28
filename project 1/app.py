from flask import Flask, request, jsonify
from flask_cors import CORS
from yt_dlp import YoutubeDL
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Define directory to store downloaded videos
DOWNLOAD_DIR = "videos"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def download_videos(url, download_dir, download_type):
    """Function to handle downloading based on the type of download."""
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'format': 'best',
        'retries': 10,
        'sleep-interval': 2,
        'max-sleep-interval': 5
    }

    if download_type == 'playlist':
        ydl_opts['yesplaylist'] = True

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_videos_in_batches(url, download_dir, batch_size=20):
    """Function to download channel videos in batches to handle large volumes."""
    current_start = 1
    while True:
        ydl_opts = {
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'format': 'best',
            'playliststart': current_start,
            'playlistend': current_start + batch_size - 1,
            'retries': 10,
            'sleep-interval': 2,
            'max-sleep-interval': 5
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])
        
        # Break if there are no more videos to download
        if result is None:
            break
        
        # Move to the next batch
        current_start += batch_size

@app.route('/download', methods=['POST'])
def download():
    """API endpoint to handle download requests."""
    data = request.get_json()
    url = data.get('channelUrl', '').strip()
    download_type = data.get('downloadType', '').strip()

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        # Call batch download function if downloading all channel videos
        if download_type == 'channel':
            download_videos_in_batches(url, DOWNLOAD_DIR, batch_size=20)
        else:
            download_videos(url, DOWNLOAD_DIR, download_type)

        return jsonify({'message': f'{download_type.capitalize()} download started successfully.'})

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'An error occurred while downloading.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
