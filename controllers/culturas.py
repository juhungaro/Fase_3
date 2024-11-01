from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Cultura
from db_config import get_db

router = APIRouter(prefix="/Culturas", tags=["Culturas"])

# Cria uma nova cultura
@router.post('/culturas/')
def create_cultura(nome: str, db: Session = Depends(get_db)):
    db_cultura = Cultura(nome=nome)
    db.add(db_cultura)
    db.commit()
    db.refresh(db_cultura)
    return db_cultura

# Obtem uma cultura por ID
@router.get("/culturas/{idcultura}")
def read_cultura(idcultura: int, db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    return cultura

# Lista todas as culturas
@router.get("/culturas/")
def read_culturas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    culturas = db.query(Cultura).offset(skip).limit(limit).all()
    return culturas