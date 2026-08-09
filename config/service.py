import json

def load_message_data():
    with open("config/message.json", "r") as f:
        data = json.load(f)
    return data


def load_conversation_data():
    with open("config/conversation.json", "r") as f:
        data = json.load(f)
    return data

def save_conversation_data(data):
    with open("config/conversation.json", "w") as f:
        json.dump(data, f)

def save_message_data(data):
    with open("config/message.json", "w") as f:
        json.dump(data, f)

