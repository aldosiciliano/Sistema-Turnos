import enum
from sqlalchemy import Column, Integer, DateTime, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base import Base

class EstadoTurno(str, enum.Enum):
    Pendiente = "Pendiente"
    Confirmado = "Confirmado"
    Cancelado = "Cancelado"
    Atendido  = "Atendido"

class Turno(Base):
    __tablename__ = "turnos"

    id_turno = Column(Integer, primary_key=True, autoincrement=True)

    id_paciente = Column(
        Integer,
        ForeignKey("pacientes.id_paciente", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )
    id_profesional = Column(
        Integer,
        ForeignKey("profesionales.id_profesional", onupdate="CASCADE", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )

    fecha_hora = Column(DateTime, nullable=False)
    estado = Column(Enum(EstadoTurno, name="estado_turno_enum", native_enum=True),
                    nullable=False, default=EstadoTurno.Pendiente)
    observaciones = Column(Text)

    paciente = relationship("Paciente", back_populates="turnos")
    profesional = relationship("Profesional", back_populates="turnos")