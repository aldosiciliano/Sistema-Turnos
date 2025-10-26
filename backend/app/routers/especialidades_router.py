from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.sessions import get_session
from app.models.especialidad import Especialidad
from app.schemas.especialidades_schemas import EspecialidadCreate, EspecialidadOut

router = APIRouter(prefix="/especialidades", tags=["Especialidades"])

# Crear una especialidad
@router.post("/", response_model=EspecialidadOut)
async def crear_especialidad(datos: EspecialidadCreate, db: AsyncSession = Depends(get_session)):
    nueva = Especialidad(nombre=datos.nombre)
    db.add(nueva)
    await db.commit()
    await db.refresh(nueva)
    return nueva


# Listar todas las especialidades
@router.get("/", response_model=list[EspecialidadOut])
async def listar_especialidades(db: AsyncSession = Depends(get_session)):
    res = await db.execute(select(Especialidad))
    return res.scalars().all()
