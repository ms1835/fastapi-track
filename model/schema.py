from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional

class ConversationSchema(BaseModel):
    id: Annotated[str, Field(..., description="The unique identifier for the conversation")]
    participants: Annotated[list[ParticipantSchema], Field(..., description="List of participants in the conversation")]
    type: Annotated[Literal["group", "direct"], Field(..., description="The type of conversation, either 'group' or 'direct'")]
    title: Annotated[Optional[str], Field(None, description="The title of the conversation, applicable for group conversations")]
    status: Annotated[Literal["active", "resolved"], Field(..., description="The status of the conversation, either 'active' or 'resolved'")]
    created_at: Annotated[str, Field(..., description="The timestamp when the conversation was created")]
    updated_at: Annotated[str, Field(..., description="The timestamp when the conversation was last updated")]


class ParticipantSchema(BaseModel):
    user_id: Annotated[str, Field(..., description="The unique identifier for the participant")]
    name: Annotated[str, Field(..., description="The name of the participant")]
    email: Annotated[str, Field(..., description="The email address of the participant")]


class MessageSchema(BaseModel):
    message_id: Annotated[str, Field(..., description="The unique identifier for the message")]
    conversation_id: Annotated[str, Field(..., description="The ID of the conversation to which the message belongs")]
    sender_id: Annotated[str, Field(..., description="The ID of the participant who sent the message")]
    content: Annotated[str, Field(..., description="The content of the message")]
    message_type: Annotated[Literal["text", "image", "video"], Field(..., description="The type of the message, either 'text', 'image', or 'video'")]
    created_at: Annotated[str, Field(..., description="The timestamp when the message was created")]
    read_at: Annotated[Optional[str], Field(None, description="The timestamp when the message was read, if applicable")]
    status: Annotated[Literal["sent", "delivered", "read"], Field(..., description="The status of the message, either 'sent', 'delivered', or 'read'")]
    