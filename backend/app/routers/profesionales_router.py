from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.sessions import get_session
from app.models.profesional import Profesional
from app.schemas.profesionales_schemas import ProfesionalCreate, ProfesionalOut

router = APIRouter(prefix="/profesionales", tags=["Profesionales"])

# Crear un profesional
@router.post("/", response_model=ProfesionalOut)
async def crear_profesional(datos: ProfesionalCreate, db: AsyncSession = Depends(get_session)):
    nuevo = Profesional(**datos.model_dump())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo


# Listar todos los profesionales
@router.get("/", response_model=list[ProfesionalOut])
async def listar_profesionales(db: AsyncSession = Depends(get_session)):
    res = await db.execute(select(Profesional))
    return res.scalars().all()
