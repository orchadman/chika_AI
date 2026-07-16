import keyboard
import threading
import time
import queue
import re
import os

# Store the physical pywebview window instance
ui_window = None

def init_window(window_instance):
    """Called by main.py to link the physical UI window."""
    global ui_window
    ui_window = window_instance

def set_speaking_state(is_speaking):
    """Directly injects the Javascript boolean into the browser memory."""
    if ui_window:
        try:
            js_code = "speaking = true;" if is_speaking else "speaking = false;"
            ui_window.evaluate_js(js_code)
        except Exception:
            pass 

# Create a thread-safe bucket for text
speech_queue = queue.Queue()
speaker = None

def clean_text_for_speech(text):
    """Strips markdown and code blocks so she speaks naturally."""
    text = re.sub(r'[*_#~`]', '', text)
    text = re.sub(r'```.*?```', ' [Code Block Generated] ', text, flags=re.DOTALL)
    return text

def tts_worker():
    """Handles all voice generation safely within its own dedicated thread."""
    global speaker
    
    # ===================================================
    # 1. INITIALIZE SAPI5 FALLBACK FIRST (THREAD SAFE)
    # ===================================================
    try:
        import pythoncom
        import win32com.client
        pythoncom.CoInitialize() # CRITICAL: Allows COM in background thread
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        
        # Try to find a female voice
        for voice in speaker.GetVoices():
            if "Zira" in voice.GetDescription() or "Female" in voice.GetDescription():
                speaker.Voice = voice
                break
        speaker.Rate = 2 
    except Exception as e:
        print(f"[SYSTEM] Could not load Native SAPI5 Fallback: {e}")

    # ===================================================
    # 2. ATTEMPT TO LOAD KOKORO NEURAL VOICE
    # ===================================================
    VOICE_ID = "bf_emma"
    kokoro = None
    TTS_ENGINE = "SAPI5"
    
    try:
        from kokoro_onnx import Kokoro
        import sounddevice as sd
        
        model_path = os.path.join(os.path.dirname(__file__), "kokoro-v0_19.onnx")
        voices_path = os.path.join(os.path.dirname(__file__), "voices.json")
        
        if os.path.exists(model_path) and os.path.exists(voices_path):
            kokoro = Kokoro(model_path, voices_path)
            TTS_ENGINE = "KOKORO"
            print(f"[SYSTEM] Neural Voice Engine ({VOICE_ID}) Loaded Successfully.")
        else:
            print(f"[WARNING] Neural Voice skipped: Model files missing in C:\\CHIKA.")
            
    except Exception as e:
        print(f"[WARNING] Neural libraries missing or invalid: {e}. Falling back to SAPI5.")

    # ===================================================
    # 3. THE AUDIO PROCESSING LOOP
    # ===================================================
    while True:
        text = speech_queue.get()
        try:
            clean_text = clean_text_for_speech(text)
            if not clean_text.strip():
                continue
                
            set_speaking_state(True)

            if TTS_ENGINE == "KOKORO" and kokoro:
                # Generate Neural Audio
                samples, sample_rate = kokoro.create(clean_text, voice=VOICE_ID, speed=1.1, lang="en-gb")
                chunk_size = int(sample_rate * 0.1) 
                
                with sd.OutputStream(samplerate=sample_rate, channels=1, dtype='float32') as sd_stream:
                    for i in range(0, len(samples), chunk_size):
                        sd_stream.write(samples[i:i+chunk_size])
            else:
                # Fallback to SAPI5
                if speaker:
                    speaker.Speak(clean_text, 1)
                    while speaker.Status.RunningState == 2:
                        time.sleep(0.1)
                        
        except Exception as e:
            print(f"\n[TTS ERROR] {e}")
        finally:
            set_speaking_state(False)
            speech_queue.task_done()

# Start her vocal cords immediately
threading.Thread(target=tts_worker, daemon=True).start()

def lock_microphone():
    pass 

def interrupt_speech():
    """Instantly silences Chika."""
    global speaker
    with speech_queue.mutex:
        speech_queue.queue.clear()
        
    if speaker is not None:
        try:
            speaker.Speak("", 2) 
        except:
            pass
            
    set_speaking_state(False)

def speak_boot(text):
    """Drops text into the speech bucket and monitors for the escape key."""
    speech_queue.put(text)
    
    def check_escape():
        while not speech_queue.empty() or (speaker and speaker.Status.RunningState == 2):
            if keyboard.is_pressed('esc'):
                print("\n[SYSTEM] Escape pressed! Silencing Chika...")
                interrupt_speech()
                break
            time.sleep(0.1)
            
    threading.Thread(target=check_escape, daemon=True).start()