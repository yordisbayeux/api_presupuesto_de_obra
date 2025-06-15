from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models, schemas
from ..auth.auth import get_current_user

router = APIRouter(prefix="/presupuestos", tags=["Presupuestos"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{presupuesto_id}/capitulos", response_model=list[schemas.CapituloOut])
def get_capitulos(presupuesto_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    joins = (
        db.query(models.Capitulo)
        .join(models.PresupuestoCapitulo, models.PresupuestoCapitulo.id_capitulo == models.Capitulo.id_capitulo)
        .filter(models.PresupuestoCapitulo.id_presupuesto == presupuesto_id)
        .all()
    )
    return joins