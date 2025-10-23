from pydantic import BaseModel

class ProfesionalCreate(BaseModel):
    nombre: str
    apellido: str
    matricula: str
    id_especialidad: int

class ProfesionalOut(BaseModel):
    id_profesional: int
    nombre: str
    apellido: str
    matricula: str
    id_especialidad: int

    class Config:
        from_attributes = True