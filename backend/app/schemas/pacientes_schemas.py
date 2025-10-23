from pydantic import BaseModel
from datetime import date

class PacienteCreate(BaseModel):
    nombre: str
    apellido: str
    dni: str
    telefono: str
    fecha_nacimiento: date

class PacienteOut(BaseModel):
    id_paciente: int
    nombre: str
    apellido: str
    dni: str
    telefono: str
    fecha_nacimiento: date

    class Config:
        from_attributes = True