from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models, schemas
from ..auth.auth import get_current_user

router = APIRouter(prefix="/capitulos", tags=["Capitulos"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{capitulo_id}", response_model=schemas.CapituloOut)
def get_capitulo(capitulo_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return db.query(models.Capitulo).filter(models.Capitulo.id_capitulo == capitulo_id).first()
