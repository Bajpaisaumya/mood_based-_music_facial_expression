# Mood-Based Music Recommendation System

A Python-based music recommendation system that detects a user's facial emotion in real time and recommends songs accordingly using the Spotify API.

## Project Overview

This project combines **Computer Vision**, **Emotion Detection**, and **Music Recommendation** to create a smart system that suggests songs based on the user's current mood.  
It captures facial expressions through a webcam, predicts the detected emotion, and then fetches suitable music recommendations.

The goal of this project is to build an interactive application that connects **AI/ML concepts** with a real-world use case in entertainment and personalization.

## Features

- Real-time face detection using webcam
- Emotion recognition from facial expressions
- Song recommendation based on detected mood
- Spotify API integration for music suggestions
- User-friendly interface with Tkinter
- Class-based Python implementation

## Tech Stack

- **Programming Language:** Python
- **Libraries/Frameworks:** OpenCV, DeepFace, Tkinter
- **API:** Spotify API
- **Concepts Used:** Computer Vision, Emotion Detection, Recommendation Logic

## How It Works

1. The system opens the webcam and captures the user's face.
2. Facial expression is analyzed using DeepFace.
3. The detected emotion is mapped to a suitable music mood/category.
4. The system connects to Spotify API.
5. Songs are recommended based on the detected emotion.

## Supported Emotions

The system can detect emotions such as:

- Happy
- Sad
- Angry
- Neutral
- Surprise
- Fear

## Project Structure

```bash
Mood-Based-Music-Recommendation/
│── main.py
│── requirements.txt
│── README.md
│── assets/
│── screenshots/
