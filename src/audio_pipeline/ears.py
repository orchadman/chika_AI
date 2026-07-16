import os
import speech_recognition as sr

def listen_for_wake_word():
    """Listens passively for the wake word 'Chika'. No keyboard shortcuts."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            # Short listen times for quick looping so it doesn't hang
            audio = r.listen(source, timeout=1, phrase_time_limit=3)
            text = r.recognize_google(audio).lower()
            if "chika" in text:
                return True
        except:
            pass
    return False

def listen_and_transcribe(groq_client):
    """Triggered by the UI microphone button or wake word. Uses Groq."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("\n[SYSTEM] Listening... (Speak now)")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=15)
            temp_file = "temp_audio.wav"
            
            with open(temp_file, "wb") as f:
                f.write(audio.get_wav_data())
            
            with open(temp_file, "rb") as file:
                transcription = groq_client.audio.transcriptions.create(
                    file=(temp_file, file.read()),
                    model="whisper-large-v3",
                    prompt="Transcribe the following.",
                )
            os.remove(temp_file)
            return transcription.text
        except Exception as e:
            print(f"[SYSTEM] Silence or audio error: {e}")
            return ""