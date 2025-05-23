from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid
from models.project import Project

class TeamMember(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    project_id: uuid.UUID = Field(foreign_key="project.id")
    role: str
    description: Optional[str] = None
    personality: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    project: Optional[Project] = Relationship(back_populates="team_members")
    tasks: List["Task"] = Relationship(back_populates="assigned_to")
