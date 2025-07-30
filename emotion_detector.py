from deepface import DeepFace
import streamlit as st
import cv2
import webbrowser
import tkinter as tk
from tkinter import ttk
from spotify_fetcher import init_spotify, get_top_track, emotion_to_genre
from concurrent.futures import ThreadPoolExecutor
import time

class MoodRecommender:
    def __init__(self):
        self.sp = init_spotify()
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    def get_language(self):
        """Quick language selection GUI."""
        result = [None]
        
        def select(lang):
            result[0] = lang
            root.destroy()
        
        root = tk.Tk()
        root.title("Language")
        root.geometry("250x120")
        root.eval('tk::PlaceWindow . center')
        
        tk.Label(root, text=" Choose Language:", font=("Arial", 12)).pack(pady=10)
        
        frame = tk.Frame(root)
        frame.pack(pady=10)
        
        ttk.Button(frame, text="🇮🇳 Hindi", command=lambda: select("hindi")).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame, text="🇺🇸 English", command=lambda: select("english")).pack(side=tk.LEFT, padx=5)
        
        root.mainloop()
        return result[0]
    
    def capture_face(self):
        """Capture image with face detection."""
        cam = cv2.VideoCapture(0)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        print("Press SPACE to capture (ESC to cancel)")
        frame_count = 0
        
        while True:
            ret, frame = cam.read()
            if not ret: break
            
            frame = cv2.flip(frame, 1)
       
            if frame_count % 5 == 0:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
            
        
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            cv2.putText(frame, f"Faces: {len(faces)} | SPACE=Capture", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.imshow("Mood Detector", frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 32 and len(faces) > 0:  
                cv2.imwrite("temp.jpg", frame)
                break
            elif key == 27: 
                cam.release()
                cv2.destroyAllWindows()
                return None
            
            frame_count += 1
        
        cam.release()
        cv2.destroyAllWindows()
        return "temp.jpg"
    
    def detect_emotion(self, img_path):
        """Fast emotion detection with concurrent attempts."""
        print("🔍 Detecting emotion...")
        
        def analyze():
            try:
                result = DeepFace.analyze(img_path, actions=['emotion'], enforce_detection=False)
                return result[0]['emotion'] if isinstance(result, list) else result['emotion']
            except:
                return None
        
        with ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(analyze) for _ in range(3)]
            results = [f.result() for f in futures if f.result()]
        
        if not results:
            print(" Could not detect emotion")
            return None
        

        emotion_scores = {}
        for result in results:
            for emotion, score in result.items():
                emotion_scores.setdefault(emotion, []).append(score)
        
        avg_scores = {e: sum(s)/len(s) for e, s in emotion_scores.items()}
        dominant = max(avg_scores, key=avg_scores.get)
        
        return dominant, avg_scores[dominant], avg_scores
    
    def recommend_song(self, emotion, language):
        """Get song recommendation and open in browser."""
        genre = emotion_to_genre.get(emotion.lower(), "pop")
        track_name, track_url = get_top_track(self.sp, genre, language)
        
        if track_name:
            print(f"\n Mood: {emotion}")
            print(f" Genre: {genre}")
            print(f" Song: {track_name}")
            webbrowser.open(track_url)
            return True
        return False
    
    def run_session(self):
        """Single detection session."""

        language = self.get_language()
        if not language:
            return False
        
    
        img_path = self.capture_face()
        if not img_path:
            return False

        emotion_data = self.detect_emotion(img_path)
        if not emotion_data:
            return False
        
        emotion, confidence, all_emotions = emotion_data

        print(f"\n{'='*50}")
        print(f" Detected: {emotion.upper()} ({confidence:.1f}%)")
        
        top_3 = sorted(all_emotions.items(), key=lambda x: x[1], reverse=True)[:3]
        for i, (e, s) in enumerate(top_3, 1):
            print(f"{i}. {e.capitalize()}: {s:.1f}%")
        
        print(f"{'='*50}")
        
     
        if self.recommend_song(emotion, language):
            print(" Song opened in browser!")
        else:
            print(" No song found")
    
        return True
    
    def run(self):
        """Main application loop."""
        print("🎵 Emotion-Based Song Recommender")
        print("=" * 40)
        
        try:
            while True:
                success = self.run_session()
                if success:
                    print("\n Session complete!")
                
                if input("\nTry again? (y/n): ").lower() != 'y':
                    break
        except KeyboardInterrupt:
            print("\n\nExiting...")
        
        print("\n Thanks for using the app!")

def main():
    MoodRecommender().run()

if __name__ == "__main__":
    main()