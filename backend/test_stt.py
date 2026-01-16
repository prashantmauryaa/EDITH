import os
import io
import asyncio
from dotenv import load_dotenv
from deepgram import DeepgramClient, PrerecordedOptions

load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

def test_deepgram():
    try:
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)
        
        # Create a dummy audio file (silence) or just try to hit the API with something invalid to check auth/connection
        # Or better, read a small valid wav file if exists. 
        # Since I don't have one, I'll try to send some garbage bytes but expect a specific error, 
        # OR just initialize and print.
        
        print("Deepgram Client initialized.")
        
        # Testing the specific call structure
        # Invalid audio will error, but we want to know if the METHOD exists.
        try:
             # Just checking if the chain exists
             deepgram.listen.prerecorded.v("1")
             print("Deepgram v1 method chain seems valid.")
        except Exception as attribute_err:
             print(f"Deepgram method structure error: {attribute_err}")

    except Exception as e:
        print(f"Deepgram Error: {e}")

if __name__ == "__main__":
    test_deepgram()
