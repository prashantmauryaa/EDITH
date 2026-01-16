import os
from dotenv import load_dotenv
from deepgram import DeepgramClient

load_dotenv()

def debug_deepgram():
    try:
        deepgram = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))
        print(f"Deepgram Client: {deepgram}")
        print(f"Listen/Speak attributes: {dir(deepgram)}")
        
        if hasattr(deepgram, 'listen'):
            print("--- Deepgram.listen attributes ---")
            for attr in dir(deepgram.listen):
                if not attr.startswith("_"):
                    print(attr)
            print("----------------------------------")
            try:
                print(f"Listen.rest attributes: {dir(deepgram.listen.rest)}")
            except Exception as e:
                print(f"No listen.rest: {e}")
            
            try:
                print(f"Listen.prerecorded attributes: {dir(deepgram.listen.prerecorded)}")
            except:
                print("No listen.prerecorded")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_deepgram()
