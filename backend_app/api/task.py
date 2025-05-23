from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from schemas.task import TaskCreate, TaskRead
from crud.task import create_task, get_task_by_id, list_project_tasks
from uuid import UUID

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/project/{project_id}", response_model=TaskRead)
def create_new_task(project_id: UUID, task: TaskCreate, session: Session = Depends(get_session)):
    return create_task(session, project_id, task)

@router.get("/{task_id}", response_model=TaskRead)
def read_task(task_id: UUID, session: Session = Depends(get_session)):
    task = get_task_by_id(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/project/{project_id}", response_model=list[TaskRead])
def project_tasks(project_id: UUID, session: Session = Depends(get_session)):
    return list_project_tasks(session, project_id)
