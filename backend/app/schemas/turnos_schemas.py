from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class EstadoTurno(str, Enum):
    Pendiente = "Pendiente"
    Confirmado = "Confirmado"
    Cancelado = "Cancelado"
    Atendido = "Atendido"

class TurnoCreate(BaseModel):
    id_paciente: int
    id_profesional: int
    fecha_hora: datetime
    observaciones: str

class TurnoOut(BaseModel):
    id_turno: int
    id_paciente: int
    id_profesional: int
    fecha_hora: datetime
    estado: EstadoTurno
    observaciones: str

    class Config:
        from_attributes = True
