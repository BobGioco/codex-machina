from sqlmodel import Session, select
from models.message import Message
from schemas.message import MessageCreate
from uuid import uuid4
from datetime import datetime

def create_message(session: Session, project_id: UUID, message_create: MessageCreate) -> Message:
    message = Message(
        id=uuid4(),
        project_id=project_id,
        sender=message_create.sender,
        content=message_create.content,
        role=message_create.role,
        timestamp=datetime.utcnow()
    )
    session.add(message)
    session.commit()
    session.refresh(message)
    return message

def list_project_messages(session: Session, project_id: UUID):
    return session.exec(select(Message).where(Message.project_id == project_id).order_by(Message.timestamp)).all()
