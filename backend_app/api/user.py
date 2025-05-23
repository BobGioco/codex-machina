from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from schemas.user import UserCreate, UserRead
from crud.user import create_user, get_user_by_id
from uuid import UUID

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserRead)
def register_user(user_create: UserCreate, session: Session = Depends(get_session)):
    return create_user(session, user_create)

@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: UUID, session: Session = Depends(get_session)):
    user = get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
