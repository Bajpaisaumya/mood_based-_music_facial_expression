
import streamlit as st
import cv2
import numpy as np
from deepface import DeepFace
from urllib.parse import quote_plus


# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Mood-Based Music Recommender",
    page_icon="🎵",
    layout="centered"
)


# ==========================================
# 2. EMOTION TO GENRE MAPPING
# ==========================================

emotion_to_genre = {
    "happy": "pop upbeat music",
    "sad": "lofi relaxing music",
    "angry": "calm instrumental music",
    "neutral": "acoustic music",
    "fear": "peaceful ambient music",
    "surprise": "energetic music",
    "disgust": "relaxing music"
}


# ==========================================
# 3. LANGUAGE MAPPING
# ==========================================

language_map = {
    "English": "English",
    "Hindi": "Hindi",
    "Punjabi": "Punjabi",
    "Korean": "Korean",
    "Instrumental": "Instrumental"
}


# ==========================================
# 4. YOUTUBE SEARCH FUNCTION
# ==========================================

def get_youtube_search(emotion, language):

    genre = emotion_to_genre.get(
        emotion.lower(),
        "relaxing music"
    )

    selected_language = language_map.get(
        language,
        "English"
    )

    search_query = f"{selected_language} {genre}"

    encoded_query = quote_plus(search_query)

    youtube_url = (
        "https://www.youtube.com/results"
        f"?search_query={encoded_query}"
    )

    return search_query, youtube_url


# ==========================================
# 5. IMAGE PROCESSING
# ==========================================

def process_image(uploaded_image):

    image_bytes = uploaded_image.getvalue()

    image_array = np.frombuffer(
        image_bytes,
        dtype=np.uint8
    )

    image = cv2.imdecode(
        image_array,
        cv2.IMREAD_COLOR
    )

    if image is None:
        raise ValueError("Unable to read captured image.")

    return image


# ==========================================
# 6. EMOTION DETECTION
# ==========================================

def detect_emotion(image):

    result = DeepFace.analyze(
        img_path=image,
        actions=["emotion"],
        enforce_detection=True
    )

    if isinstance(result, list):
        result = result[0]

    emotions = result["emotion"]

    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    return dominant_emotion, emotions


# ==========================================
# 7. MAIN APPLICATION
# ==========================================

def main():

    st.title("🎵 Mood-Based Music Recommender")

    st.write(
        "Discover music recommendations "
        "based on your facial expressions."
    )

    st.info(
        "Note: Facial expressions provide an estimate "
        "and do not necessarily represent actual emotions."
    )

    st.divider()

    # Language selection

    language = st.selectbox(
        "🌐 Select your preferred language",
        list(language_map.keys())
    )

    # Camera input

    st.subheader("📸 Capture Your Face")

    uploaded_image = st.camera_input(
        "Take a picture using your camera"
    )

    if uploaded_image is not None:

        # Display captured image

        st.image(
            uploaded_image,
            caption="Captured Image",
            use_container_width=True
        )

        # Analyze button

        if st.button("🔍 Analyze My Expression"):

            try:

                with st.spinner(
                    "Analyzing facial expression..."
                ):

                    image = process_image(uploaded_image)

                    emotion, scores = detect_emotion(image)

                # Display detected emotion

                st.success(
                    f"Detected Facial Expression: {emotion.upper()}"
                )

                # Emotion scores

                st.subheader("📊 Emotion Analysis")

                st.bar_chart(scores)

                # Music recommendation

                song_name, youtube_url = get_youtube_search(
                    emotion,
                    language
                )

                genre = emotion_to_genre.get(
                    emotion.lower(),
                    "relaxing music"
                )

                st.divider()

                st.subheader("🎧 Your Music Recommendation")

                st.write("**Expression:**", emotion)

                st.write("**Music Category:**", genre)

                st.write("**Language:**", language)

                st.write("**Search Query:**", song_name)

                # YouTube link

                st.link_button(
                    "▶ Find Music on YouTube",
                    youtube_url
                )

                st.success(
                    "Your music recommendation is ready!"
                )

            except ValueError as e:

                st.error(
                    f"Image processing error: {e}"
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# ==========================================
# 8. APPLICATION ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()
