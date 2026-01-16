import os
import sys
from deepgram import DeepgramClient
from dotenv import load_dotenv

load_dotenv()

try:
    dg = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))
    if hasattr(dg, 'listen'):
        with open("deepgram_debug.txt", "w") as f:
            f.write(f"Listen type: {type(dg.listen)}\n")
            f.write(f"Listen dir: {dir(dg.listen)}\n")
            try: 
                 f.write(f"v1.media dir: {dir(dg.listen.v1.media)}\n")
            except Exception as e:
                 f.write(f"No v1.media: {e}\n")
    else:
        print("No listen attr")
except Exception as e:
    import traceback
    traceback.print_exc()
    print(e)
