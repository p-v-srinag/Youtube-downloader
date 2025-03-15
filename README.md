**YouTube Downloader**

This is a simple web application that allows users to download all videos from a specified YouTube channel URL. The application is built using Flask (a lightweight web framework for Python) and yt-dlp (a YouTube video downloader).

**Features**
Downloads all videos from a given YouTube channel URL.
Uses yt-dlp, a popular command-line tool, to handle the actual video downloading.
Saves videos locally on your machine.
Built with Flask for easy web interaction.

**Prerequisites**
Before you begin, ensure you have met the following requirements:

Python 3.6 or higher.
pip (Python package manager).
A valid YouTube channel URL.

**Installation**
Clone the repository to your local machine:

    git clone https://github.com/p-v-srinag/Youtube-downloader.git
    cd Youtube-downloader
Create a virtual environment (optional but recommended):

    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required Python packages:

    pip install -r requirements.txt
    Install yt-dlp (if not included in requirements.txt):

    pip install yt-dlp
    
**Usage**

Run the Flask app:

    python app.py
    
Enter the YouTube channel URL in the provided input box and click "Download."

The application will begin downloading all videos from the channel to your local machine.

Contributing

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Create a new Pull Request.
