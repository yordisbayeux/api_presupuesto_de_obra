from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas
from ..auth.auth import get_current_user

router = APIRouter(prefix="/partidas", tags=["Partidas"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/capitulo/{capitulo_id}", response_model=list[schemas.PartidaOut])
def get_partidas(capitulo_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return (
        db.query(models.Partida)
        .join(models.PresupuestoCapitulo)
        .filter(models.PresupuestoCapitulo.id_capitulo == capitulo_id)
        .all()
    )

@router.put("/{partida_id}", response_model=schemas.PartidaOut)
def update_partida(partida_id: int, data: schemas.PartidaUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    partida = db.query(models.Partida).filter(models.Partida.id_partida == partida_id).first()
    if not partida:
        raise HTTPException(status_code=404, detail="Partida no encontrada")
    if data.precio_unitario_base is not None:
        partida.precio_unitario_base = data.precio_unitario_base
    if data.margen_partida is not None:
        partida.margen_partida = data.margen_partida
    db.commit()
    db.refresh(partida)
    return partida