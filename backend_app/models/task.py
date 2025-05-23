from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid
from models.project import Project
from models.team_member import TeamMember

class Task(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    project_id: uuid.UUID = Field(foreign_key="project.id")
    assigned_to_id: Optional[uuid.UUID] = Field(default=None, foreign_key="teammember.id")
    title: str
    description: Optional[str] = None
    status: str = Field(default="pending")
    result_summary: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    project: Optional[Project] = Relationship(back_populates="tasks")
    assigned_to: Optional[TeamMember] = Relationship(back_populates="tasks")
