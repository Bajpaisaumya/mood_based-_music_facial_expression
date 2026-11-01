# 🎵 Mood-Based Music Recommendation System

## Project Overview

The Mood-Based Music Recommendation System is a Python-based application that uses Computer Vision and facial emotion analysis to recommend music according to detected facial expressions.

The application captures a user's facial image through a webcam, analyzes facial expressions using DeepFace, identifies the dominant emotion, and generates relevant music recommendations based on the detected emotion and preferred language.

## Key Features

- Real-time webcam image capture using OpenCV.
- Facial emotion analysis using DeepFace.
- Detection of emotions such as Happy, Sad, Angry, Neutral, and Fear.
- Emotion-to-genre mapping.
- Language-based music recommendations.
- YouTube search link generation.
- Interactive interface using Streamlit.

## Technology Stack

- Python
- OpenCV
- DeepFace
- Streamlit
- urllib
- YouTube Search URL

## System Workflow

1. User selects a preferred music language.
2. Webcam captures the user's facial image.
3. DeepFace analyzes the facial expression.
4. The dominant emotion is identified.
5. The emotion is mapped to a music genre.
6. A language-specific music search query is generated.
7. The user receives a YouTube search link.

## Emotion-Based Recommendation

| Detected Emotion | Music Genre |
|---|---|
| Happy | Pop |
| Sad | Lofi |
| Angry | Rock |
| Neutral | Acoustic |
| Fear | Ambient |

## Supported Languages

- English
- Hindi
- Punjabi
- Korean
- Instrumental

## Future Improvements

- Integrate YouTube Data API for fetching actual video results.
- Improve the recommendation engine.
- Display multiple song recommendations.
- Add music preferences and user feedback.
- Improve webcam integration with Streamlit.
- Add better error handling and testing.

## Project Objective

To explore the integration of Computer Vision, facial emotion analysis, and music recommendation techniques in an interactive Python application.
