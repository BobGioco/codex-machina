from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid
from models.project import Project

class Message(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    project_id: uuid.UUID = Field(foreign_key="project.id")
    sender: str
    content: str
    role: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    project: Optional[Project] = Relationship(back_populates="messages")
