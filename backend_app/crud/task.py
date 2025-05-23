from sqlmodel import Session, select
from models.task import Task
from schemas.task import TaskCreate
from uuid import uuid4
from datetime import datetime

def create_task(session: Session, project_id: UUID, task_create: TaskCreate) -> Task:
    task = Task(
        id=uuid4(),
        project_id=project_id,
        title=task_create.title,
        description=task_create.description,
        assigned_to_id=task_create.assigned_to_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_task_by_id(session: Session, task_id: UUID) -> Task:
    return session.get(Task, task_id)

def list_project_tasks(session: Session, project_id: UUID):
    return session.exec(select(Task).where(Task.project_id == project_id)).all()
