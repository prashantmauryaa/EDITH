import os
import inspect
from deepgram import DeepgramClient
from dotenv import load_dotenv

load_dotenv()

try:
    dg = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))
    method = dg.listen.v1.media.transcribe_file
    print(f"Method: {method}")
    print("SIG_START")
    print(f"Signature: {inspect.signature(method)}")
    print("SIG_END")
    print(f"Doc: {method.__doc__}")
except Exception as e:
    print(f"Error: {e}")
