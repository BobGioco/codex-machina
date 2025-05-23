from fastapi import FastAPI
from database import init_db
from api import user, project, task, team_member, message

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(users.router)
app.include_router(project.router)
app.include_router(task.router)
app.include_router(team_member.router)
app.include_router(message.router)