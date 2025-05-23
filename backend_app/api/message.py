from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from schemas.message import MessageCreate, MessageRead
from crud.message import create_message, list_project_messages
from uuid import UUID

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.post("/project/{project_id}", response_model=MessageRead)
def post_message(project_id: UUID, message: MessageCreate, session: Session = Depends(get_session)):
    return create_message(session, project_id, message)

@router.get("/project/{project_id}", response_model=list[MessageRead])
def get_messages(project_id: UUID, session: Session = Depends(get_session)):
    return list_project_messages(session, project_id)
