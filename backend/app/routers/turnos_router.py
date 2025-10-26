from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.sessions import get_session
from app.models.turno import Turno
from app.schemas.turnos_schemas import TurnoCreate, TurnoOut

router = APIRouter()

# Crear un nuevo turno
@router.post("/", response_model=TurnoOut)
async def crear_turno(datos: TurnoCreate, db: AsyncSession = Depends(get_session)):
    nuevo_turno = Turno(**datos.model_dump())
    db.add(nuevo_turno)
    await db.commit()
    await db.refresh(nuevo_turno)
    return nuevo_turno

# Listar todos los turnos
@router.get("/", response_model=list[TurnoOut])
async def listar_turnos(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Turno))
    return result.scalars().all()
