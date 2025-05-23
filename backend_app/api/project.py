from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from schemas.project import ProjectCreate, ProjectRead
from crud.project import create_project, get_project_by_id, list_user_projects
from uuid import UUID

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectRead)
def create_new_project(project: ProjectCreate, user_id: UUID, session: Session = Depends(get_session)):
    return create_project(session, project, user_id)

@router.get("/{project_id}", response_model=ProjectRead)
def read_project(project_id: UUID, session: Session = Depends(get_session)):
    project = get_project_by_id(session, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.get("/user/{user_id}", response_model=list[ProjectRead])
def user_projects(user_id: UUID, session: Session = Depends(get_session)):
    return list_user_projects(session, user_id)
