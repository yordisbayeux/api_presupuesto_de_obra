from pydantic import BaseModel
from typing import Optional

class ObraOut(BaseModel):
    id_obra: int
    nombre: str
    referencia: str
    class Config:
        orm_mode = True

class PresupuestoOut(BaseModel):
    id_presupuesto: int
    nombre_presupuesto: str
    class Config:
        orm_mode = True

class CapituloOut(BaseModel):
    id_capitulo: int
    descripcion: str
    class Config:
        orm_mode = True

class PartidaOut(BaseModel):
    id_partida: int
    descripcion: str
    precio_unitario_base: float
    margen_partida: float
    cantidad: float
    class Config:
        orm_mode = True

class PartidaUpdate(BaseModel):
    precio_unitario_base: Optional[float]
    margen_partida: Optional[float]

class UserCreate(BaseModel):
    username: str
    password: str