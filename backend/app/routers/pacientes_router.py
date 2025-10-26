from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.sessions import get_session
from app.models.paciente import Paciente
from app.schemas.pacientes_schemas import PacienteCreate, PacienteOut

router = APIRouter()

@router.post("/", response_model=PacienteOut)
async def crear_paciente(datos: PacienteCreate, db: AsyncSession = Depends(get_session)):
    nuevo = Paciente(**datos.model_dump())
    db.add(nuevo)
    await db.commit()
    await db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[PacienteOut])
async def listar_pacientes(db: AsyncSession = Depends(get_session)):
    result = await db.execute(select(Paciente))
    return result.scalars().all()


# 🟢 Obtener por ID
@router.get("/{id_paciente}", response_model=PacienteOut)
async def obtener_paciente(id_paciente: int, db: AsyncSession = Depends(get_session)):
    res = await db.execute(select(Paciente).where(Paciente.id_paciente == id_paciente))
    paciente = res.scalar_one_or_none()
    if not paciente:
        raise HTTPException(404, "Paciente no encontrado")
    return paciente

# 🔴 Eliminar por ID
@router.delete("/{id_paciente}")
async def eliminar_paciente(id_paciente: int, db: AsyncSession = Depends(get_session)):
    res = await db.execute(select(Paciente).where(Paciente.id_paciente == id_paciente))
    paciente = res.scalar_one_or_none()
    if not paciente:
        raise HTTPException(404, "Paciente no encontrado")
    await db.delete(paciente)
    await db.commit()
    return {"mensaje": "Paciente eliminado correctamente"}