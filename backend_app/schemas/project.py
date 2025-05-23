from pydantic import BaseModel
from typing import Optional, Dict
from uuid import UUID

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    tech_stack: Optional[Dict] = None
    repo_url: Optional[str] = None

class ProjectRead(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    tech_stack: Optional[Dict] = None
    repo_url: Optional[str] = None
    status: str

    class Config:
        orm_mode = True