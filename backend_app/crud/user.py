from sqlmodel import Session, select
from models.user import User
from schemas.user import UserCreate
from uuid import uuid4
import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(session: Session, user_create: UserCreate) -> User:
    user = User(
        id=uuid4(),
        email=user_create.email,
        hashed_password=hash_password(user_create.password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user