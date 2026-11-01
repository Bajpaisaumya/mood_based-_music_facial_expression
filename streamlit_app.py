
import streamlit as st
import numpy as np
from PIL import Image
from deepface import DeepFace
from urllib.parse import quote_plus


# --------------------------------
# 1. Emotion to Music Genre Mapping
# --------------------------------

emotion_to_genre = {
    "happy": "pop upbeat music",
    "sad": "lofi relaxing music",
    "angry": "calm instrumental music",
    "neutral": "acoustic music",
    "fear": "peaceful ambient music",
    "surprise": "energetic music",
    "disgust": "relaxing music"
}


# --------------------------------
# 2. Language Mapping
# --------------------------------

language_map = {
    "english": "English",
    "hindi": "Hindi",
    "punjabi": "Punjabi",
    "korean": "Korean",
    "instrumental": "Instrumental"
}


# --------------------------------
# 3. Generate YouTube Search Link
# --------------------------------

def get_local_song(emotion, language):

    genre = emotion_to_genre.get(
        emotion.lower(),
        "relaxing music"
    )

    selected_language = language_map.get(
        language.lower(),
        "English"
    )

    song = f"{selected_language} {genre}"

    search_query = quote_plus(song)

    url = (
        "https://www.youtube.com/results"
        f"?search_query={search_query}"
    )

    return song, url


# --------------------------------
# 4. Emotion Detection
# --------------------------------

def detect_emotion(image_array):

    result = DeepFace.analyze(
        img_path=image_array,
        actions=["emotion"],
        enforce_detection=False
    )

    if isinstance(result, list):
        result = result[0]

    emotions = result["emotion"]

    dominant_emotion = max(
        emotions,
        key=emotions.get
    )

    return dominant_emotion, emotions


# --------------------------------
# 5. Main Streamlit Application
# --------------------------------

def main():

    st.set_page_config(
        page_title="Mood-Based Music Recommender",
        page_icon="🎵",
        layout="centered"
    )

    st.title("🎵 Mood-Based Music Recommender")

    st.write(
        "Discover music recommendations based on "
        "your facial expressions!"
    )

    st.divider()

    # Language selection

    language = st.selectbox(
        "🌐 Choose your preferred language",
        [
            "english",
            "hindi",
            "punjabi",
            "korean",
            "instrumental"
        ]
    )

    st.subheader("📸 Capture Your Face")

    # Streamlit camera input

    img = st.camera_input("Take a picture")

    if img is not None:

        # Convert uploaded image to RGB NumPy array

        image = Image.open(img).convert("RGB")

        image_array = np.array(image)

        st.image(
            image,
            caption="Captured Image",
            use_container_width=True
        )

        try:

            with st.spinner(
                "Analyzing facial expression..."
            ):

                emotion, scores = detect_emotion(
                    image_array
                )

            st.success(
                f"Detected Facial Expression: {emotion.upper()}"
            )

            # Emotion visualization

            st.subheader("📊 Emotion Analysis")

            st.bar_chart(scores)

            # Music recommendation

            track_name, track_url = get_local_song(
                emotion,
                language
            )

            genre = emotion_to_genre.get(
                emotion.lower(),
                "relaxing music"
            )

            st.divider()

            st.subheader("🎧 Music Recommendation")

            st.write("**Detected Emotion:**", emotion)

            st.write("**Recommended Genre:**", genre)

            st.write("**Selected Language:**", language)

            st.markdown(
                f"### 🎵 {track_name}"
            )

            st.link_button(
                "▶ Search Music on YouTube",
                track_url
            )

        except Exception as e:

            st.error(
                f"Unable to analyze the image: {e}"
            )


# --------------------------------
# 6. Application Entry Point
# --------------------------------

if __name__ == "__main__":
    main()
