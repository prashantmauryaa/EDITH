import json
import os
from datetime import datetime

class MemoryManager:
    def __init__(self, filepath="edith_memory.json"):
        self.filepath = filepath
        self.conversation_history = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading memory: {e}")
                return []
        return []

    def save_interaction(self, user_text, ai_response):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user_text,
            "assistant": ai_response
        }
        self.conversation_history.append(entry)
        
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving memory: {e}")

    def get_recent_context(self, limit=5):
        """Returns the last 'limit' interactions formatted for the AI context."""
        context = []
        recent = self.conversation_history[-limit:]
        
        for entry in recent:
            context.append({"role": "user", "content": entry["user"]})
            context.append({"role": "assistant", "content": entry["assistant"]})
            
        return context
