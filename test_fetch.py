from spotify_fetcher import init_spotify, emotion_to_genre, get_top_track

emotion = "happy"
genre = emotion_to_genre.get(emotion, "pop")

sp = init_spotify()
name, url = get_top_track(sp, genre)

print(f"\n🎧 Emotion: {emotion}")
print(f"🎵 Genre: {genre}")
print(f"🎶 Playlist: {name}")
print(f"🔗 URL: {url}")
