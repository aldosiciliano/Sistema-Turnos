from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Especialidad(Base):
    __tablename__ = "especialidades"

    id_especialidad = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)

    profesionales = relationship("Profesional", back_populates="especialidad")
