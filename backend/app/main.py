from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.sessions import get_session, engine
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Clinica API (DB Check)")

@app.on_event("startup")
async def startup_check():
    # Chequeo rápido al iniciar (opcional)
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))

@app.get("/")
def root():
    return {"status": "ok"}
