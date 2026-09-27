import streamlit as st
import cv2
from deepface import DeepFace
from urllib.parse import quote_plus


emotion_to_genre = {
    "happy": "pop",
    "sad": "lofi",
    "angry": "rock",
    "neutral": "acoustic",
    "fear": "ambient"
}


def get_local_song(emotion, language):
    songs = {
        "happy": {
            "english": "Happy Pop Music",
            "hindi": "Hindi Happy Songs",
            "punjabi": "Punjabi Happy Songs"
        },
        "sad": {
            "english": "Relaxing Lofi Music",
            "hindi": "Hindi Lofi Sad Songs",
            "punjabi": "Punjabi Lofi Songs"
        },
        "angry": {
            "english": "Rock Music",
            "hindi": "Hindi Rock Songs",
            "punjabi": "Punjabi Rock Songs"
        },
        "neutral": {
            "english": "Relaxing Acoustic Music",
            "hindi": "Hindi Acoustic Songs",
            "punjabi": "Punjabi Acoustic Songs"
        },
        "fear": {
            "english": "Calm Ambient Music",
            "hindi": "Calm Hindi Music",
            "punjabi": "Calm Punjabi Music"
        }
    }

    song = songs.get(emotion.lower(), {}).get(
        language.lower(),
        "Relaxing Music"
    )

    search_query = quote_plus(song)
    url = f"https://www.youtube.com/results?search_query={search_query}"

    return song, url
def capture_image():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        st.error("Failed to access camera.")
        return None

    st.info("Press SPACE to capture, ESC to exit.")

    while True:
        ret, frame = cam.read()

        if not ret:
            st.error("Failed to read frame from camera.")
            cam.release()
            cv2.destroyAllWindows()
            return None

        cv2.imshow("Press SPACE to Capture", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == 32:  # SPACE
            cv2.imwrite("captured.jpg", frame)
            cam.release()
            cv2.destroyAllWindows()
            return "captured.jpg"

        elif key == 27:  # ESC
            cam.release()
            cv2.destroyAllWindows()
            return None

def detect_emotion(img_path):
    result = DeepFace.analyze(img_path, actions=['emotion'], enforce_detection=False)
    emotions = result[0]['emotion'] if isinstance(result, list) else result['emotion']
    dominant = max(emotions, key=emotions.get)
    return dominant, emotions

def main():
    st.title("🎵 Mood-Based Music Recommender")
    language = st.selectbox("🌐 Choose your preferred language", ["english", "hindi", "punjabi", "korean", "instrumental"])

    
    if st.button("📸 Capture Face"):
        img_path = capture_image()
        if img_path:
            st.success("Image captured!")
            st.image(img_path, caption="Captured Face", use_container_width=True)
            
            st.info("Detecting emotion...")
            emotion, scores = detect_emotion(img_path)
            st.success(f"Detected Emotion: {emotion}")
            
            genre = emotion_to_genre.get(emotion.lower(), "pop")
            track_name, track_url = get_local_song(emotion, language)
            st.write("Genre:", genre)
            st.write("Language:", language)
            st.write("Track Name:", track_name)
            st.write("Track URL:", track_url)

            if track_url:
                st.markdown(f"🎧 **Recommended Song:** [{track_name}]({track_url})", unsafe_allow_html=True)
            else:
                st.warning("⚠️ No song found for this mood. Try a different expression.")

if __name__ == "__main__":
    main()
