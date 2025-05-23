from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid
from models.user import User

class Project(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    name: str
    description: Optional[str] = None
    tech_stack: Optional[dict] = None
    repo_url: Optional[str] = None
    status: str = Field(default="active")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship(back_populates="projects")
    team_members: List["TeamMember"] = Relationship(back_populates="project")
    tasks: List["Task"] = Relationship(back_populates="project")
    messages: List["Message"] = Relationship(back_populates="project")