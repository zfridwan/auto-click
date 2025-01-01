import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Inisialisasi pyttsx3 untuk text-to-speech
engine = pyttsx3.init()

# Fungsi untuk mengucapkan teks
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fungsi untuk mendengarkan perintah suara
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengarkan...")
        recognizer.adjust_for_ambient_noise(source)  # Menyesuaikan dengan kebisingan sekitar
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="id-ID")
        print(f"Perintah yang didengar: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Tidak dapat mengenali perintah.")
        return ""
    except sr.RequestError:
        print("Terjadi kesalahan pada layanan pengenalan suara.")
        return ""

# Fungsi untuk menjalankan perintah
def run_command(command):
    if 'halo' in command:
        speak("Halo, ada yang bisa saya bantu?")
    elif 'waktu' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sekarang jam {current_time}")
    elif 'buka' in command:
        if 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Membuka YouTube.")
        elif 'google' in command:
            webbrowser.open("https://www.google.com")
            speak("Membuka Google.")
    elif 'berhenti' in command or 'keluar' in command:
        speak("Terima kasih, sampai jumpa!")
        exit()
    else:
        speak("Perintah tidak dikenali, coba lagi.")

# Main loop
if __name__ == "__main__":
    speak("Halo, saya asisten virtual. Apa yang bisa saya bantu?")
    while True:
        command = listen()
        if command:
            run_command(command)