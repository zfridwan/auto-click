import speech_recognition as sr
from gtts import gTTS
# import os
import pyttsx3

engine = pyttsx3.init()

# Function to speak text in Indonesian using gTTS
def speak(text):
    """Speak the given text in Indonesian using gTTS."""
    tts = gTTS(text=text, lang="id")
    # tts.save("output.mp3")
    # os.system("start output.mp3")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for audio input and convert it to text (Indonesian)."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengarkan...")
        try:
            audio = recognizer.listen(source)
            print("Mengenali...")
            return recognizer.recognize_google(audio, language="id-ID")
        except sr.UnknownValueError:
            print("Maaf, saya tidak bisa memahami audio.")
            speak("Maaf, saya tidak bisa memahami audio.")
            return None
        except sr.RequestError as e:
            print(f"Tidak dapat meminta hasil; {e}")
            speak("Tidak dapat meminta hasil.")
            return None

# Predefined list of registered names (in Indonesian)
registered_names = ["Alice", "Budi", "Charlie"]

def main():
    print("Sebutkan nama untuk memeriksa apakah sudah terdaftar.")
    while True:
        name = listen()
        if name:
            print(f"Anda mengatakan: {name}")
            if name in registered_names:
                print(f"{name} sudah terdaftar.")
                speak(f"{name} sudah terdaftar.")
            else:
                print("Nama tersebut belum terdaftar.")
                speak("Nama tersebut belum terdaftar.")

if __name__ == "__main__":
    main()
