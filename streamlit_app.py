import streamlit as st
import cv2
from deepface import DeepFace
from spotify_fetcher import init_spotify, get_top_track, emotion_to_genre
import webbrowser

sp = init_spotify()

def capture_image():
    cam = cv2.VideoCapture(0)
    st.info("Press SPACE to capture, ESC to exit.")
    while True:
        ret, frame = cam.read()
        if not ret:
            st.error("Failed to access camera.")
            break
        cv2.imshow("Press SPACE to Capture", frame)
        key = cv2.waitKey(1)
        if key == 32:  # SPACE
            cv2.imwrite("captured.jpg", frame)
            break
        elif key == 27:  # ESC
            cam.release()
            cv2.destroyAllWindows()
            return None
    cam.release()
    cv2.destroyAllWindows()
    return "captured.jpg"

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
            track_name, track_url = get_top_track(sp, genre, language)
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
