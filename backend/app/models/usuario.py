import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .base import Base

class Rol(str, enum.Enum):
    admin = "admin"
    paciente = "paciente"
    profesional = "profesional"
    
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password_hash = Column(String(255), nullable=False)
    rol = Column(Enum(Rol, name="rol_enum", native_enum=True), nullable=False)

    
    paciente = relationship("Paciente", back_populates="usuario", uselist=False)
    profesional = relationship("Profesional", back_populates="usuario", uselist=False)
    
