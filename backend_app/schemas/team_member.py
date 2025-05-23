from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class TeamMemberCreate(BaseModel):
    role: str
    description: Optional[str] = None
    personality: Optional[str] = None

class TeamMemberRead(BaseModel):
    id: UUID
    role: str
    description: Optional[str]
    personality: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True