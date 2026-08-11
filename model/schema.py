from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional

class ParticipantSchema(BaseModel):
    user_id: Annotated[str, Field(..., description="The unique identifier for the participant")]
    name: Annotated[str, Field(..., description="The name of the participant")]
    email: Annotated[str, Field(..., description="The email address of the participant")]

class ConversationSchema(BaseModel):
    id: Annotated[str, Field(..., description="The unique identifier for the conversation")]
    participants: Annotated[list[ParticipantSchema], Field(..., description="List of participants in the conversation")]
    type: Annotated[Literal["group", "direct"], Field(..., description="The type of conversation, either 'group' or 'direct'")]
    title: Annotated[Optional[str], Field(None, description="The title of the conversation, applicable for group conversations")]
    status: Annotated[Literal["active", "resolved"], Field(..., description="The status of the conversation, either 'active' or 'resolved'")]
    created_at: Annotated[str, Field(..., description="The timestamp when the conversation was created")]
    updated_at: Annotated[str, Field(..., description="The timestamp when the conversation was last updated")]

class AttachmentSchema(BaseModel):
    file_name: Annotated[str, Field(..., description="The name of the attached file")]
    file_type: Annotated[str, Field(..., description="The MIME type of the attachment")]
    url: Annotated[str, Field(..., description="The URL where the attachment can be accessed")]

class MessageSchema(BaseModel):
    message_id: Annotated[str, Field(..., description="The unique identifier for the message")]
    conversation_id: Annotated[str, Field(..., description="The ID of the conversation to which the message belongs")]
    sender_id: Annotated[str, Field(..., description="The ID of the participant who sent the message")]
    receiver_ids: Annotated[list[str], Field(default_factory=list, description="List of recipient participant IDs")]
    message_type: Annotated[Literal["text", "image", "video", "notification"], Field(..., description="The type of the message")]
    content: Annotated[str, Field(..., description="The content of the message")]
    attachments: Annotated[list[AttachmentSchema], Field(default_factory=list, description="List of file attachments")]
    created_at: Annotated[str, Field(..., description="The timestamp when the message was created")]
    read_at: Annotated[Optional[str], Field(None, description="The timestamp when the message was read, if applicable")]
    status: Annotated[Literal["sent", "delivered", "read"], Field(..., description="The status of the message")]

class CreateMessageSchema(BaseModel):
    message_id: Annotated[str, Field(..., description="The unique identifier for the message")]
    sender_id: Annotated[str, Field(..., description="The ID of the participant who sent the message")]
    receiver_ids: Annotated[list[str], Field(default_factory=list, description="List of recipient participant IDs")]
    message_type: Annotated[Literal["text", "image", "video", "notification"], Field(..., description="The type of the message")]
    content: Annotated[str, Field(..., description="The content of the message")]
    attachments: Annotated[list[AttachmentSchema], Field(default_factory=list, description="List of file attachments")]
    created_at: Annotated[str, Field(..., description="The timestamp when the message was created")]
    read_at: Annotated[Optional[str], Field(None, description="The timestamp when the message was read, if applicable")]
    status: Annotated[Literal["sent", "delivered", "read"], Field(..., description="The status of the message")]

class UpdateMessageSchema(BaseModel):
    receiver_ids: Annotated[list[str], Field(default_factory=list, description="Updated receiver IDs for the message")]
    content: Annotated[str, Field(..., description="Updated content of the message")]
    