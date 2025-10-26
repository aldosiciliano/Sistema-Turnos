from pydantic import BaseModel

class ProfesionalCreate(BaseModel):
    nombre: str
    apellido: str
    matricula: str
    id_especialidad: int
    id_usuario: int | None = None

class ProfesionalOut(BaseModel):
    id_profesional: int
    nombre: str
    apellido: str
    matricula: str
    id_especialidad: int
    id_usuario: int | None = None

    class Config:
        from_attributes = True
