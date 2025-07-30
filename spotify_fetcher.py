

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import random


emotion_to_genre = {
    "happy": "pop",
    "sad": "lofi",
    "angry": "rock",
    "neutral": "acoustic",
    "fear": "ambient"
}

def init_spotify():
    client_id = "8339f5ca8dfa4bc6b29375cd96dc64e5"      
    client_secret = "7a6d617e7b4e4d44a74ce6b7f49f2c32" 

    if "your_client_id_here" in client_id or "your_client_secret_here" in client_secret:
        raise ValueError(" Please replace client_id and client_secret.")

    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

def get_top_track(sp, genre, language="english"):
    try:
        query = f"{language} {genre}"
        results = sp.search(q=query, type='track', limit=10)
        items = results['tracks']['items']
        if items:
            track = random.choice(items)
            name = track['name']
            artist = track['artists'][0]['name']
            url = track['external_urls']['spotify']
            return f"{name} by {artist}", url
        return None, None
    except Exception as e:
        print("Error fetching track:", e)
        return None, None
