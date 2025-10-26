from pydantic import BaseModel

class EspecialidadCreate(BaseModel):
    nombre: str

class EspecialidadOut(BaseModel):
    id_especialidad: int
    nombre: str

    class Config:
        from_attributes = True
