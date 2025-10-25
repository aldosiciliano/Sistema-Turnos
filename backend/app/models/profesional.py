from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Profesional(Base):
    __tablename__ = "profesionales"

    id_profesional = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    matricula = Column(String(50), nullable=False)

    id_especialidad = Column(
        Integer,
        ForeignKey("especialidades.id_especialidad", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False
    )
    especialidad = relationship("Especialidad", back_populates="profesionales")

    id_usuario = Column( 
        Integer,
        ForeignKey("usuarios.id_usuario", onupdate="CASCADE", ondelete="CASCADE"),
        unique=True,
        nullable=True
    )
    usuario = relationship("Usuario", back_populates="profesional", uselist=False)

    turnos = relationship("Turno", back_populates="profesional")
