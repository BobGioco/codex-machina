from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid

class User(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    api_keys: Optional[dict] = None
    preferences: Optional[dict] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    projects: List["Project"] = Relationship(back_populates="user")

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

class TeamMember(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    project_id: uuid.UUID = Field(foreign_key="project.id")
    role: str
    description: Optional[str] = None
    personality: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    project: Optional[Project] = Relationship(back_populates="team_members")
    tasks: List["Task"] = Relationship(back_populates="assigned_to")

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

class Message(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    project_id: uuid.UUID = Field(foreign_key="project.id")
    sender: str
    content: str
    role: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    project: Optional[Project] = Relationship(back_populates="messages")
