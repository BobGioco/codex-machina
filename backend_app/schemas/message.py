from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class MessageCreate(BaseModel):
    sender: str  # 'user', 'project_leader', 'agent'
    content: str
    role: Optional[str] = None

class MessageRead(BaseModel):
    id: UUID
    sender: str
    content: str
    role: Optional[str] = None
    timestamp: datetime

    class Config:
        orm_mode = True