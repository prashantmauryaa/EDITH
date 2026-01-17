# EDITH - Advanced Terminal Voice Assistant

EDITH is a high-performance, real-time voice AI assistant designed to run directly in your terminal. It features advanced Hinglish (Hindi + English) understanding, long-term memory, and a witty personality.

## 🚀 Features

*   **Real-time Voice Interaction**: Talk to EDITH naturally with low latency.
*   **Hinglish Support**: seamless understanding of mixed Hindi and English commands (e.g., "Kaise ho?", "Code run nahi ho raha").
*   **Long-Term Memory**: EDITH remembers your past conversations and context across sessions. It saves interactions locally in `edith_memory.json`.
*   **Premium Voices**: Uses ElevenLabs for lifelike, human-sounding responses (Rachel voice).
*   **Intelligent Brain**: Powered by Groq (Llama 3.3 70B) for instant, smart, and witty responses.

## 🛠️ Tech Stack

*   **Brain (LLM)**: Groq (Llama 3.3 70B)
*   **Ears (STT)**: Deepgram Nova-2 (Optimized for Indian English/Hinglish)
*   **Voice (TTS)**: ElevenLabs (Streamed audio)
*   **Language**: Python
*   **Memory**: Local JSON-based persistent storage

## 📦 Setup

1.  **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd EDITH
    ```

2.  **Install Dependencies**:
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

3.  **Environment Setup**:
    Create a `.env` file in the `backend/` directory with your API keys:
    ```env
    GROQ_API_KEY=your_groq_key
    DEEPGRAM_API_KEY=your_deepgram_key
    ELEVENLABS_API_KEY=your_elevenlabs_key
    ```

## ▶️ How to Run

Simply double-click **`run_edith.bat`** or run it from the terminal:

```bash
.\run_edith.bat
```

EDITH will initialize, calibrate to your background noise, and greet you with:
*"EDITH is online, ready to help you sir."*

##  Usage Tips

*   **Speak Normally**: You don't need to shout. The mic is calibrated for conversational volume.
*   **Hinglish**: Feel free to use Hindi conversational words like "yar", "kya hal hai", "samjha nahi".
*   **Stop**: Press `Ctrl+C` to exit. EDITH will say "Goodbye sir" before closing.
