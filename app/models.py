from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric, Boolean, Text, DateTime, func
from sqlalchemy.orm import relationship
from .database import Base

class TProvincia(Base):
    __tablename__ = "TProvincia"
    id_provincia = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100), nullable=False)
    poblacion = Column(String(100))
    created_at = Column(DateTime, default=func.now())

class TEstadoObra(Base):
    __tablename__ = "TEstadoObra"
    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

class TCliente(Base):
    __tablename__ = "TCliente"
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    descripcion = Column(Text)
    correo = Column(String(150))
    telefono = Column(String(20))
    website = Column(String(200))
    año_fundacion = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class TMoneda(Base):
    __tablename__ = "TMoneda"
    id_moneda = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(50), nullable=False)
    codigo = Column(String(3), unique=True, nullable=False)
    simbolo = Column(String(5))
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

class TEstadoPresupuesto(Base):
    __tablename__ = "TEstadoPresupuesto"
    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

class TUnidadMedida(Base):
    __tablename__ = "TUnidadMedida"
    id_unidad_medida = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(50), nullable=False)
    abreviatura = Column(String(10))
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

class TProveedores(Base):
    __tablename__ = "TProveedores"
    id_proveedor = Column(Integer, primary_key=True, autoincrement=True)
    nombre_empresa = Column(String(200), nullable=False)
    sitio_web = Column(String(200))
    id_provincia = Column(Integer, ForeignKey("TProvincia.id_provincia"))
    calificacion = Column(Numeric(3,2))
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class TElementos(Base):
    __tablename__ = "TElementos"
    id_elemento = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(300), nullable=False)
    id_unidad_medida = Column(Integer, ForeignKey("TUnidadMedida.id_unidad_medida"))
    precio_unitario_referencia = Column(Numeric(10,4))
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

class Obra(Base):
    __tablename__ = "TObras"
    id_obra = Column(Integer, primary_key=True, autoincrement=True)
    referencia = Column(String(50), unique=True, nullable=False)
    nombre = Column(String(200), nullable=False)
    direccion = Column(String(300))
    id_provincia = Column(Integer, ForeignKey("TProvincia.id_provincia"))
    pais = Column(String(100), default='España')
    id_estado = Column(Integer, ForeignKey("TEstadoObra.id_estado"))
    id_cliente = Column(Integer, ForeignKey("TCliente.id_cliente"))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    coste_total_previsto = Column(Numeric(15,2))
    coste_total_real = Column(Numeric(15,2))
    beneficio_teorico = Column(Numeric(15,2))
    version = Column(String(20), default='1.0')
    tipo_actividad = Column(String(100))
    tamaño = Column(String(50))
    facturacion = Column(Numeric(15,2))
    nota = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    presupuestos = relationship("Presupuesto", back_populates="obra")

class Presupuesto(Base):
    __tablename__ = "TPresupuestos"
    id_presupuesto = Column(Integer, primary_key=True, autoincrement=True)
    id_obra = Column(Integer, ForeignKey("TObras.id_obra"), nullable=False)
    nombre_presupuesto = Column(String(200), nullable=False)
    id_estado = Column(Integer, ForeignKey("TEstadoPresupuesto.id_estado"))
    fecha_inicio = Column(Date)
    fecha_fin = Column(Date)
    id_moneda = Column(Integer, ForeignKey("TMoneda.id_moneda"))
    fecha_creacion = Column(DateTime, default=func.now())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    obra = relationship("Obra", back_populates="presupuestos")
    capitulos = relationship("PresupuestoCapitulo", back_populates="presupuesto")

class Capitulo(Base):
    __tablename__ = "TCapitulos"
    id_capitulo = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200), nullable=False)
    orden = Column(Integer)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

class PresupuestoCapitulo(Base):
    __tablename__ = "PresupuestoCapitulo"
    id_presupuesto_capitulo = Column(Integer, primary_key=True, autoincrement=True)
    id_presupuesto = Column(Integer, ForeignKey("TPresupuestos.id_presupuesto"), nullable=False)
    id_capitulo = Column(Integer, ForeignKey("TCapitulos.id_capitulo"), nullable=False)
    orden = Column(Integer)
    costo_total_capitulo = Column(Numeric(15,2))

    presupuesto = relationship("Presupuesto", back_populates="capitulos")
    partidas = relationship("Partida", back_populates="presupuesto_capitulo")

class Partida(Base):
    __tablename__ = "TPartidas"
    id_partida = Column(Integer, primary_key=True, autoincrement=True)
    id_presupuesto_capitulo = Column(Integer, ForeignKey("PresupuestoCapitulo.id_presupuesto_capitulo"), nullable=False)
    codigo = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(300), nullable=False)
    id_unidad_medida = Column(Integer, ForeignKey("TUnidadMedida.id_unidad_medida"))
    cantidad = Column(Numeric(10,3))
    precio_unitario_base = Column(Numeric(10,4))
    margen_partida = Column(Numeric(5,2))
    costo_total = Column(Numeric(15,2))
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

    presupuesto_capitulo = relationship("PresupuestoCapitulo", back_populates="partidas")

class PartidasElementos(Base):
    __tablename__ = "PartidasElementos"
    id_partida_elemento = Column(Integer, primary_key=True, autoincrement=True)
    id_partida = Column(Integer, ForeignKey("TPartidas.id_partida"), nullable=False)
    id_elemento = Column(Integer, ForeignKey("TElementos.id_elemento"), nullable=False)
    cantidad = Column(Numeric(10,3))
    precio_unitario = Column(Numeric(10,4))
    id_proveedor = Column(Integer, ForeignKey("TProveedores.id_proveedor"))

class Usuario(Base):
    __tablename__ = "TUsuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)