from enum import Enum
from pydantic import BaseModel, EmailStr

# Enum de roles
class Rol(str, Enum):
    admin = "admin"
    paciente = "paciente"
    profesional = "profesional"

# Schema base para crear usuario
class UsuarioCreate(BaseModel):
    email: EmailStr
    password: str
    rol: Rol

# Schema para devolver usuario
class UsuarioOut(BaseModel):
    id_usuario: int
    email: EmailStr
    rol: Rol

    class Config:
        from_attributes = True  # Permite devolver objetos de SQLAlchemy