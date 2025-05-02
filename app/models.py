from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    role: str
    content: str

class AdviceRequest(BaseModel):
    conversation: List[Message]
    players: list[str] | None = None

class AdviceResponse(BaseModel):
    reply: str
