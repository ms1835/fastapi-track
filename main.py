from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from config.service import load_conversation_data, load_message_data, save_conversation_data, save_message_data

app = FastAPI()

@app.get("/")
def load_home_page():
    return {"message": "Welcome to the Notification Service API!"}

@app.get("/conversations/{conversation_id}")
def get_conversation(conversation_id: str = Path(..., description="The ID of the conversation to retrieve")):
    conversations = load_conversation_data()
    conversation = next((c for c in conversations if c["id"] == conversation_id), None)
    if conversation:
        return JSONResponse(status_code=200, content=conversation)
    raise HTTPException(status_code=404, detail="Conversation not found")