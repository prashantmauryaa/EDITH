
import os
import sys
import asyncio
import traceback
import speech_recognition as sr
import pygame
import io
from dotenv import load_dotenv
from groq import Groq
from deepgram import DeepgramClient
from elevenlabs.client import ElevenLabs

# Load environment variables
load_dotenv()

# Colors for terminal output
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Initialize constants
# Initialize constants
SYSTEM_PROMPT = (
    "You are EDITH, a highly advanced AI assistant. "
    "You speak in a mix of English and Hindi (Hinglish). "
    "Your personality is witty, sarcastic, and slightly superior but helpful. "
    "Keep your answers concise (under 2-3 sentences) unless asked otherwise. "
    "Don't be boring."
)
RACHEL_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"

print(f"{YELLOW}Initializing EDITH Terminal Mode...{RESET}")

# Initialize Clients
try:
    groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    deepgram_client = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))
    elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
    print(f"{GREEN}Clients initialized successfully.{RESET}")
except Exception as e:
    print(f"{GREEN}Error initializing clients: {e}{RESET}")
    sys.exit(1)

import pyttsx3

# ... existing code ...

# Initialize Pygame Mixer for audio playback
try:
    pygame.mixer.init()
except Exception as e:
    print(f"Error initializing audio player: {e}")

# Initialize Local TTS (Fallback)
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Try to select a female voice if available
    for voice in voices:
        if "female" in voice.name.lower() or "ziroh" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
except Exception as e:
    print(f"Local TTS Init Error: {e}")
    engine = None

def listen_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{BLUE}EDITH is listening... (Speak now){RESET}")
        r.adjust_for_ambient_noise(source, duration=0.5) 
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print(f"{YELLOW}Thinking...{RESET}")
            return audio.get_wav_data()
        except sr.WaitTimeoutError:
            # print("No speech detected.") # Reduce noise
            return None
        except Exception as e:
            print(f"Mic error: {e}")
            return None

def transcribe(audio_bytes):
    if not audio_bytes:
        return None
    
    try:
        source = {"buffer": audio_bytes, "mimetype": "audio/wav"}
        # Deepgram Nova-2
        options = {
            "model": "nova-2",
            "smart_format": True,
            "language": "en-IN"
        }
        response = deepgram_client.listen.v1.media.transcribe_file(source, options)
        transcript = response.results.channels[0].alternatives[0].transcript
        return transcript
    except Exception as e:
        print(f"Transcription error: {e}")
        return None

def get_ai_response(text, history):
    history.append({"role": "user", "content": text})
    try:
        completion = groq_client.chat.completions.create(
            messages=history,
            model="llama3-8b-8192",
        )
        response = completion.choices[0].message.content
        history.append({"role": "assistant", "content": response})
        return response, history
    except Exception as e:
        print(f"AI Error: {e}")
        return None, history

def speak(text):
    print(f"{GREEN}EDITH Speaking...{RESET}")
    
    # Try ElevenLabs first
    try:
        audio_stream = elevenlabs_client.text_to_speech.convert(
            text=text,
            voice_id=RACHEL_VOICE_ID,
            model_id="eleven_turbo_v2_5"
        )
        
        audio_data = b"".join(audio_stream)
        
        if audio_data:
            sound_file = io.BytesIO(audio_data)
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            return

    except Exception as e:
        print(f"{YELLOW}ElevenLabs Error (switching to fallback): {e}{RESET}")
    
    # Fallback to pyttsx3
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Fallback TTS Error: {e}")
    else:
        print("No TTS available.")

def main():
    history = [{"role": "system", "content": SYSTEM_PROMPT}]
    print(f"{GREEN}EDITH is Online. Press Ctrl+C to exit.{RESET}")
    
    try:
        while True:
            # 1. Listen
            audio_bytes = listen_mic()
            if not audio_bytes:
                continue
            
            # 2. Transcribe
            text = transcribe(audio_bytes)
            if not text or not text.strip():
                print("Could not understand audio.")
                continue
            
            print(f"{BLUE}You said: {text}{RESET}")
            
            # 3. Think
            response, history = get_ai_response(text, history)
            if not response:
                continue
            
            print(f"{GREEN}EDITH: {response}{RESET}")
            
            # 4. Speak
            speak(response)
            
    except KeyboardInterrupt:
        print("\nGoodbye, Boss!")
    except Exception as e:
        print(f"Fatal Error: {e}")

if __name__ == "__main__":
    main()
