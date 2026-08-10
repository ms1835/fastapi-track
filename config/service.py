import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CONVERSATIONS_PATH = DATA_DIR / "conversations.json"
MESSAGES_PATH = DATA_DIR / "messages.json"


def load_message_data():
    with open(MESSAGES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_conversation_data():
    with open(CONVERSATIONS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_conversation_data(data):
    with open(CONVERSATIONS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def save_message_data(data):
    with open(MESSAGES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

