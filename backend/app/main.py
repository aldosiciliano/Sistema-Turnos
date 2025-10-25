from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.sessions import get_session, engine
from dotenv import load_dotenv
from app.routers import auth_router

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


#Rutas

#app.include_router(pacientes_router, prefix="/pacientes")
#app.include_router(turnos_router, prefix="/turnos")
app.include_router(auth_router  )