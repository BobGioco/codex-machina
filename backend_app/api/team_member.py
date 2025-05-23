from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from schemas.team_member import TeamMemberCreate, TeamMemberRead
from crud.team_member import create_team_member, get_team_member_by_id, list_project_members
from uuid import UUID

router = APIRouter(prefix="/team", tags=["Team Members"])

@router.post("/project/{project_id}", response_model=TeamMemberRead)
def create_member(project_id: UUID, member: TeamMemberCreate, session: Session = Depends(get_session)):
    return create_team_member(session, project_id, member)

@router.get("/{member_id}", response_model=TeamMemberRead)
def read_member(member_id: UUID, session: Session = Depends(get_session)):
    member = get_team_member_by_id(session, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Team member not found")
    return member

@router.get("/project/{project_id}", response_model=list[TeamMemberRead])
def project_members(project_id: UUID, session: Session = Depends(get_session)):
    return list_project_members(session, project_id)
