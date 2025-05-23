from sqlmodel import Session, select
from models.project import Project
from schemas.project import ProjectCreate
from uuid import uuid4

def create_project(session: Session, project_create: ProjectCreate, user_id: UUID) -> Project:
    project = Project(
        id=uuid4(),
        user_id=user_id,
        name=project_create.name,
        description=project_create.description,
        tech_stack=project_create.tech_stack,
        repo_url=project_create.repo_url
    )
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

def get_project_by_id(session: Session, project_id: UUID) -> Project:
    return session.get(Project, project_id)

def list_user_projects(session: Session, user_id: UUID):
    return session.exec(select(Project).where(Project.user_id == user_id)).all()
