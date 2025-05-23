from sqlmodel import Session, select
from models.team_member import TeamMember
from schemas.team_member import TeamMemberCreate
from uuid import uuid4
from datetime import datetime

def create_team_member(session: Session, project_id: UUID, member_create: TeamMemberCreate) -> TeamMember:
    member = TeamMember(
        id=uuid4(),
        project_id=project_id,
        role=member_create.role,
        description=member_create.description,
        personality=member_create.personality,
        created_at=datetime.utcnow()
    )
    session.add(member)
    session.commit()
    session.refresh(member)
    return member

def get_team_member_by_id(session: Session, member_id: UUID) -> TeamMember:
    return session.get(TeamMember, member_id)

def list_project_members(session: Session, project_id: UUID):
    return session.exec(select(TeamMember).where(TeamMember.project_id == project_id)).all()
