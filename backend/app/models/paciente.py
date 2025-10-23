from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    id_paciente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    dni = Column(String(20), nullable=False)
    telefono = Column(String(20))
    fecha_nacimiento = Column(Date)

    id_usuario = Column(
        Integer,
        ForeignKey("usuarios.id_usuario", onupdate="CASCADE", ondelete="CASCADE"),
        unique=True,
        nullable=True
    )
    
    usuario = relationship("Usuario", back_populates="paciente", uselist=False)
    turnos = relationship("Turno", back_populates="paciente")
    
    