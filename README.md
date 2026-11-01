# 🎵 Mood-Based Music Recommendation System

## Project Overview

A Python-based application that uses Computer Vision and facial emotion analysis to recommend music based on detected facial expressions.

The application captures an image through a webcam, analyzes facial expressions using DeepFace, identifies the dominant emotion, and generates language-based music recommendations with YouTube search links.

## Features

- Facial image capture using Streamlit.
- Facial emotion analysis using DeepFace.
- Detection of seven facial expression categories.
- Emotion-based music genre mapping.
- Multiple language preferences.
- Emotion score visualization.
- YouTube music search integration.

## Tech Stack

- Python
- Streamlit
- OpenCV
- DeepFace
- NumPy
- Pandas
- Pillow

## Workflow

1. Select preferred music language.
2. Capture facial image using webcam.
3. Analyze facial expressions using DeepFace.
4. Identify dominant facial expression.
5. Map detected expression to a music genre.
6. Generate a language-specific YouTube search link.

## Emotion-Based Music Mapping

| Facial Expression | Music Category |
|---|---|
| Happy | Pop / Upbeat |
| Sad | Lo-fi / Relaxing |
| Angry | Calm Instrumental |
| Neutral | Acoustic |
| Fear | Ambient |
| Surprise | Energetic |
| Disgust | Relaxing |

## Supported Languages

- English
- Hindi
- Punjabi
- Korean
- Instrumental

## Installation

```bash
git clone https://github.com/Bajpaisaumya/mood_based-_music_facial_expression.git

cd mood_based-_music_facial_expression

pip install -r requirements.txt
```

## Run the Application

```bash
streamlit run streamlit_app.py
```

## Future Improvements

- Integrate YouTube Data API to fetch actual video results.
- Display video thumbnails and multiple recommendations.
- Improve recommendation personalization.
- Add user feedback functionality.
- Improve application testing and error handling.

## Author

**Saumya Bajpai**

Computer Science Engineering | AIML

Interested in Artificial Intelligence, Machine Learning, Computer Vision and Generative AI.

GitHub: https://github.com/Bajpaisaumya
