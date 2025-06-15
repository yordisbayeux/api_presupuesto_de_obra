from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models, schemas
from ..auth.auth import get_current_user

router = APIRouter(prefix="/obras", tags=["Obras"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.ObraOut])
def get_obras(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(models.Obra).all()

@router.get("/{obra_id}/presupuestos", response_model=list[schemas.PresupuestoOut])
def get_presupuestos(obra_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(models.Presupuesto).filter(models.Presupuesto.id_obra == obra_id).all()