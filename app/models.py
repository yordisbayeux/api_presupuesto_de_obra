from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Obra(Base):
    __tablename__ = "TObras"
    id_obra = Column(Integer, primary_key=True)
    referencia = Column(String(50), unique=True)
    nombre = Column(String(200))

    presupuestos = relationship("Presupuesto", back_populates="obra")

class Presupuesto(Base):
    __tablename__ = "TPresupuestos"
    id_presupuesto = Column(Integer, primary_key=True)
    id_obra = Column(Integer, ForeignKey("TObras.id_obra"))
    nombre_presupuesto = Column(String(200))

    obra = relationship("Obra", back_populates="presupuestos")
    capitulos = relationship("PresupuestoCapitulo", back_populates="presupuesto")

class Capitulo(Base):
    __tablename__ = "TCapitulos"
    id_capitulo = Column(Integer, primary_key=True)
    descripcion = Column(String)

class PresupuestoCapitulo(Base):
    __tablename__ = "PresupuestoCapitulo"
    id_presupuesto_capitulo = Column(Integer, primary_key=True)
    id_presupuesto = Column(Integer, ForeignKey("TPresupuestos.id_presupuesto"))
    id_capitulo = Column(Integer, ForeignKey("TCapitulos.id_capitulo"))

    presupuesto = relationship("Presupuesto", back_populates="capitulos")
    partidas = relationship("Partida", back_populates="presupuesto_capitulo")

class Partida(Base):
    __tablename__ = "TPartidas"
    id_partida = Column(Integer, primary_key=True)
    id_presupuesto_capitulo = Column(Integer, ForeignKey("PresupuestoCapitulo.id_presupuesto_capitulo"))
    descripcion = Column(String)
    precio_unitario_base = Column(Numeric)
    margen_partida = Column(Numeric)
    cantidad = Column(Numeric)

    presupuesto_capitulo = relationship("PresupuestoCapitulo", back_populates="partidas")

class Usuario(Base):
    __tablename__ = "TUsuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    hashed_password = Column(String(255))