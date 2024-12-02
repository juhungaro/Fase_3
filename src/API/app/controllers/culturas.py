from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Cultura
from db_config import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/culturas", tags=["Culturas"])

class CulturaRequest(BaseModel):
    nome: str
    
# Cria uma nova cultura
@router.post('/', summary='Cria uma nova cultura')
def create_cultura(cultura: CulturaRequest = Body(...), db: Session = Depends(get_db)): # Obrigatório o nome da cultura ser enviado pelo body da requisição
    db_cultura = Cultura(nome=cultura.nome)
    db.add(db_cultura)
    db.commit()
    db.refresh(db_cultura)
    return {"idcultura": db_cultura.idcultura}

# Obtem uma cultura por ID
@router.get("/{idcultura}", summary='Obtem uma cultura pelo Id')
def read_cultura(idcultura: int, db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    return cultura

# Lista todas as culturas
@router.get("/", summary='Lista todas as culturas')
def read_culturas(db: Session = Depends(get_db)):
    culturas = db.query(Cultura).all()
    return culturas

# Edita uma cultura pelo Id
@router.put("/{idcultura}", summary='Edita uma cultura pelo Id')
def delete_cultura(idcultura: int, cultura: CulturaRequest = Body(...), db: Session = Depends(get_db)):
    culturaDb = db.query(Cultura).filter(Cultura.idcultura == idcultura).first()
    if culturaDb is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    
    culturaDb.nome = cultura.nome
    
    db.commit()
    return "Cultura editada"

# Deleta uma cultura pelo Id
@router.delete("/{idcultura}", summary='Deleta uma cultura pelo Id')
def delete_cultura(idcultura: int, db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")

    db.delete(cultura)
    db.commit()
    return "Cultura deletada"