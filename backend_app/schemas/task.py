from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to_id: Optional[UUID] = None

class TaskRead(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    status: str
    result_summary: Optional[str] = None
    assigned_to_id: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
