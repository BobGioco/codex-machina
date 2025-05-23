# app/main.py
from fastapi import FastAPI
from database import init_db
from api import users

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(users.router)