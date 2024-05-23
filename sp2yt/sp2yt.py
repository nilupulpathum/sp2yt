import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import pyfiglet

# Load environment variables from .env file
load_dotenv()

def print_banner():
    banner = pyfiglet.figlet_format("SP2YT")
    print(banner)
    print("by Nilupul Pathum\n")

def authenticate_spotify():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

def extract_playlist_id(playlist_link):
    match = re.match(r"https?://open\.spotify\.com/playlist/([a-zA-Z0-9]+)\\??.*", playlist_link)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid Spotify playlist link")

def get_playlist_tracks(sp, playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def extract_song_details(tracks):
    songs = []
    for item in tracks:
        track = item['track']
        title = track['name']
        artists = ", ".join([artist['name'] for artist in track['artists']])
        songs.append(f"{title} by {artists}")
    return songs

def search_youtube(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(f"ytsearch:{query}", download=False)
            video = result['entries'][0]
            return f"https://www.youtube.com/watch?v={video['id']}", video['filesize']
        except Exception as e:
            print(f"Error searching YouTube for {query}: {e}")
            return None, 0

def download_and_convert_to_mp3(youtube_link, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])

def main():
    # Print banner
    print_banner()
    playlist_link = input("Please Enter a Spotify Playlist Link: ")

    # Authenticate with Spotify
    sp = authenticate_spotify()

    # Extract playlist ID from link
    playlist_id = extract_playlist_id(playlist_link)

    # Get Spotify playlist tracks and extract song details
    tracks = get_playlist_tracks(sp, playlist_id)
    songs = extract_song_details(tracks)

    # Search for each song on YouTube and get links using parallel processing
    youtube_links = []
    total_size = 0

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_song = {executor.submit(search_youtube, song): song for song in songs}
        for future in as_completed(future_to_song):
            song = future_to_song[future]
            try:
                link, size = future.result()
                if link:
                    youtube_links.append(link)
                    total_size += size
            except Exception as exc:
                print(f"{song} generated an exception: {exc}")

    # Convert total size to MB
    total_size_mb = total_size / (1024 * 1024)

    # Show total size and ask for confirmation
    print(f"Total download size: {total_size_mb:.2f} MB")
    confirmation = input("Do you want to proceed with the download? (yes/no): ").strip().lower()

    if confirmation == 'yes':
        # Directory to save the downloaded MP3 files
        output_dir = input("Please Enter a Name for Output Directory: ")
        os.makedirs(output_dir, exist_ok=True)

        # Download and convert each YouTube video to MP3 using parallel processing
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_link = {executor.submit(download_and_convert_to_mp3, link, output_dir): link for link in youtube_links}
            for future in as_completed(future_to_link):
                link = future_to_link[future]
                try:
                    future.result()
                    print(f"Downloaded and converted: {link}")
                except Exception as exc:
                    print(f"Failed to download {link}: {exc}")
    else:
        print("Download cancelled.")


if __name__ == "main":
    main()