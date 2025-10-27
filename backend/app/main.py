from fastapi import FastAPI
from sqlalchemy import text
from app.db.sessions import engine
from dotenv import load_dotenv
from app.routers.pacientes_router import router as pacientes_router
from app.routers.auth_router import router as auth_router
from app.routers.turnos_router import router as turnos_router
from app.routers.especialidades_router import router as especialidades_router
from app.routers.profesionales_router import router as profesionales_router
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()

app = FastAPI(title="Sistema de Turnos - Backend")

@app.on_event("startup")
async def startup_check():
    # Verifica conexión con la base de datos
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))

@app.get("/")
def root():
    return {"status": "ok"}

# Registramos los routers
app.include_router(pacientes_router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(auth_router)
app.include_router(turnos_router, prefix="/turnos", tags=["Turnos"])
app.include_router(especialidades_router)
app.include_router(profesionales_router)

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
