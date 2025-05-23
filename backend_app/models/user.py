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