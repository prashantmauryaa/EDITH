
import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs

load_dotenv()

key = os.getenv("ELEVENLABS_API_KEY")
print(f"Key loaded: {key[:5]}...")


try:
    client = ElevenLabs(api_key=key)
    print("Client initialized")
    
    print("Generating audio...")
    # Use the correct method and Voice ID for Rachel
    audio_stream = client.text_to_speech.convert(
        text="Hello, this is a test of the ElevenLabs streaming API.",
        voice_id="21m00Tcm4TlvDq8ikWAM", # Rachel ID
        model_id="eleven_turbo_v2_5"
    )
    
    print("Stream received. consuming...")
    chunk_count = 0
    total_bytes = 0
    for chunk in audio_stream:
        chunk_count += 1
        total_bytes += len(chunk)
        print(f"Received chunk {chunk_count}: {len(chunk)} bytes")
        
    print(f"Success! Received {chunk_count} chunks, {total_bytes} bytes.")
    
except Exception as e:
    import traceback
    traceback.print_exc()
    print(f"Error: {e}")

