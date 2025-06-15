from pydantic import BaseModel, Field, validator
from typing import Optional
from decimal import Decimal
from datetime import date, datetime

# Schemas de entrada (Input)
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=100)
    password: str = Field(..., min_length=6)

class ObraCreate(BaseModel):
    referencia: str = Field(..., max_length=50)
    nombre: str = Field(..., max_length=200)
    direccion: Optional[str] = Field(None, max_length=300)
    id_provincia: Optional[int] = None
    pais: str = Field(default="España", max_length=100)
    id_estado: Optional[int] = None
    id_cliente: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    coste_total_previsto: Optional[Decimal] = Field(None, decimal_places=2)
    coste_total_real: Optional[Decimal] = Field(None, decimal_places=2)
    beneficio_teorico: Optional[Decimal] = Field(None, decimal_places=2)
    version: str = Field(default="1.0", max_length=20)
    tipo_actividad: Optional[str] = Field(None, max_length=100)
    tamaño: Optional[str] = Field(None, max_length=50)
    facturacion: Optional[Decimal] = Field(None, decimal_places=2)
    nota: Optional[str] = None

class PresupuestoCreate(BaseModel):
    id_obra: int
    nombre_presupuesto: str = Field(..., max_length=200)
    id_estado: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    id_moneda: Optional[int] = None

class CapituloCreate(BaseModel):
    codigo: str = Field(..., max_length=50)
    descripcion: str = Field(..., max_length=200)
    orden: Optional[int] = None
    activo: bool = Field(default=True)

class PartidaCreate(BaseModel):
    id_presupuesto_capitulo: int
    codigo: str = Field(..., max_length=50)
    descripcion: str = Field(..., max_length=300)
    id_unidad_medida: Optional[int] = None
    cantidad: Optional[Decimal] = Field(None, decimal_places=3)
    precio_unitario_base: Optional[Decimal] = Field(None, decimal_places=4)
    margen_partida: Optional[Decimal] = Field(None, decimal_places=2)
    activo: bool = Field(default=True)

# Schemas de actualización (Update)
class PartidaUpdate(BaseModel):
    precio_unitario_base: Optional[Decimal] = Field(None, decimal_places=4)
    margen_partida: Optional[Decimal] = Field(None, decimal_places=2)
    cantidad: Optional[Decimal] = Field(None, decimal_places=3)
    descripcion: Optional[str] = Field(None, max_length=300)

class ObraUpdate(BaseModel):
    referencia: Optional[str] = Field(None, max_length=50)
    nombre: Optional[str] = Field(None, max_length=200)
    direccion: Optional[str] = Field(None, max_length=300)
    id_provincia: Optional[int] = None
    pais: Optional[str] = Field(None, max_length=100)
    id_estado: Optional[int] = None
    id_cliente: Optional[int] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    coste_total_previsto: Optional[Decimal] = Field(None, decimal_places=2)
    coste_total_real: Optional[Decimal] = Field(None, decimal_places=2)
    beneficio_teorico: Optional[Decimal] = Field(None, decimal_places=2)
    version: Optional[str] = Field(None, max_length=20)
    tipo_actividad: Optional[str] = Field(None, max_length=100)
    tamaño: Optional[str] = Field(None, max_length=50)
    facturacion: Optional[Decimal] = Field(None, decimal_places=2)
    nota: Optional[str] = None

# Schemas de salida (Output)
class UserOut(BaseModel):
    id: int
    username: str
    
    class Config:
        from_attributes = True  # Reemplaza orm_mode en Pydantic v2

class ObraOut(BaseModel):
    id_obra: int
    nombre: str
    referencia: str
    direccion: Optional[str] = None
    pais: Optional[str] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    coste_total_previsto: Optional[Decimal] = None
    coste_total_real: Optional[Decimal] = None
    beneficio_teorico: Optional[Decimal] = None
    version: Optional[str] = None
    tipo_actividad: Optional[str] = None
    tamaño: Optional[str] = None
    facturacion: Optional[Decimal] = None
    nota: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class PresupuestoOut(BaseModel):
    id_presupuesto: int
    id_obra: int
    nombre_presupuesto: str
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    fecha_creacion: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class CapituloOut(BaseModel):
    id_capitulo: int
    codigo: str
    descripcion: str
    orden: Optional[int] = None
    activo: Optional[bool] = None
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class PartidaOut(BaseModel):
    id_partida: int
    id_presupuesto_capitulo: int
    codigo: str
    descripcion: str
    cantidad: Optional[Decimal] = None
    precio_unitario_base: Optional[Decimal] = None
    margen_partida: Optional[Decimal] = None
    costo_total: Optional[Decimal] = None
    activo: Optional[bool] = None
    created_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class PresupuestoCapituloOut(BaseModel):
    id_presupuesto_capitulo: int
    id_presupuesto: int
    id_capitulo: int
    orden: Optional[int] = None
    costo_total_capitulo: Optional[Decimal] = None
    
    class Config:
        from_attributes = True

# Schemas de respuesta para autenticación
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None