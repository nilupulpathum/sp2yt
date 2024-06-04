# SP2YT

SP2YT is a CLI tool that allows you to download Spotify playlists as MP3 files from YouTube.

## Features

- Fetches tracks from a Spotify playlist.
- Searches for corresponding tracks on YouTube.
- Downloads and converts YouTube videos to MP3.
- Displays the total download size and asks for user confirmation before downloading.

## Requirements

- Python 3.6 or higher
- A Spotify Developer account and API credentials
- YouTube Data API key

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/sp2yt.git
   cd sp2yt
2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt

## Setup

1. **Spotify Developer Account and API Setup**:
   - Go to the [Spotify Developer Dashboard.](https://developer.spotify.com/dashboard)
   - Log in and create a new application.
   - Note down the `Client ID` and `Client Secret`.
2. **Environment Variables**:
   - Create a `.env` file in the project root and add your Spotify and YouTube API credentials:
     ```plaintext
     SPOTIFY_CLIENT_ID='your_spotify_client_id'
     SPOTIFY_CLIENT_SECRET='your_spotify_client_secret'

## Usage

1. **Run the CLI Tool**:
   ```bash
   sp2yt
2. **Follow the prompts**:
   - Enter the Spotify playlist link when prompted.
   - The tool will fetch the playlist tracks, search for them on YouTube, and display the total download size.
   - Confirm if you want to proceed with the download.
  
## Example
```bash
$ sp2yt
       .d8888b.  8888888b.   .d8888b. Y88b   d88P 88888888888 
      d88P  Y88b 888   Y88b d88P  Y88b Y88b d88P      888     
      Y88b.      888    888        888  Y88o88P       888     
        Y888b.   888   d88P      .d88P   Y888P        888     
           Y88b. 8888888P    .od888P      888         888     
             888 888        d88P          888         888     
      Y88b  d88P 888        888           888         888     
        Y8888P   888        888888888     888         888 
Spotify to YouTube Downloader

Enter Spotify playlist link: https://open.spotify.com/playlist/xxxxxxxxxxxxxx
Total download size: 150.25 MB
Do you want to proceed with the download? (yes/no): yes
Downloaded and converted: https://www.youtube.com/watch?v=xxxxxxxxxxx
...
```
## Acknowledge

- [**Spotipy**](https://spotipy.readthedocs.io/en/2.24.0/#) for Spotify API integrations
- [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) for downloading YouTube videos
- [**Pydub**](https://github.com/jiaaro/pydub) for audio processing
- [**python-dotenv**](https://github.com/theskumar/python-dotenv) for managing environment variables


