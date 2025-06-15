from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..database import SessionLocal
from ..models import Usuario
from ..schemas import UserCreate
from ..auth.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    user_exists = db.query(Usuario).filter(Usuario.username == user.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    hashed_pw = pwd_context.hash(user.password)
    db_user = Usuario(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    return {"msg": "Usuario registrado"}
