from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from config.service import load_conversation_data, load_message_data, save_message_data
from model.schema import MessageSchema, CreateMessageSchema

app = FastAPI()

@app.get("/")
def load_home_page():
    return {"message": "Welcome to the Notification Service API!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/conversations/{conversation_id}")
def get_conversation_details(conversation_id: str = Path(..., description="The ID of the conversation to retrieve", examples="conv_1001")):
    conversations = load_conversation_data()
    conversation = next((c for c in conversations if c["conversation_id"] == conversation_id), None)
    if conversation:
        return JSONResponse(status_code=200, content=conversation)
    raise HTTPException(status_code=404, detail="Conversation not found")


@app.get("/conversations/{conversation_id}/messages")
def get_conversation_messages(conversation_id: str = Path(..., description="The ID of the conversation to retrieve messages for", examples="conv_1001")):
    messages = load_message_data()
    conversation_messages = [m for m in messages if m["conversation_id"] == conversation_id]
    if conversation_messages:
        sorted_messages = sorted(conversation_messages, key=lambda x: x["created_at"])
        return JSONResponse(status_code=200, content=sorted_messages)
    raise HTTPException(status_code=404, detail="No messages found for this conversation")


@app.get("/messages/{message_id}")
def get_message_details(message_id: str = Path(..., description="The ID of the message to retrieve", examples="msg_5058")):
    messages = load_message_data()
    message = next((m for m in messages if m["message_id"] == message_id), None)
    if message:
        return JSONResponse(status_code=200, content=message)
    raise HTTPException(status_code=404, detail="Message not found")

@app.post("/conversations/{conversation_id}/messages")
def add_message_to_conversation(conversation_id: str, message: CreateMessageSchema):
    conversations = load_conversation_data()
    if not any(c["conversation_id"] == conversation_id for c in conversations):
        raise HTTPException(status_code=404, detail="Conversation not found")

    messages = load_message_data()
    message_data = {"conversation_id": conversation_id, **message.model_dump()}
    validated_message = MessageSchema.model_validate(message_data).model_dump()

    messages.append(validated_message)
    save_message_data(messages)
    return JSONResponse(status_code=201, content={"message": "Message added successfully", "data": validated_message})