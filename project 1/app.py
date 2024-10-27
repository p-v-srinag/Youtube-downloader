from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download_videos():
    data = request.get_json()
    channel_url = data.get('channelUrl')

    if not channel_url:
        return jsonify({'error': 'No channel URL provided'}), 400

    try:
        if not os.path.exists('videos'):
            os.makedirs('videos')

        # yt-dlp options for downloading all videos in the best quality
        ydl_opts = {
            'outtmpl': 'videos/%(title)s.%(ext)s',  # Save path for videos
            'format': 'best'  # Download in best quality
        }

        # Use yt-dlp to download the videos
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([channel_url])

        return jsonify({'message': 'Videos downloaded successfully'}), 200

    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Log the error to the console
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
