from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SensorNutrientes, Cultura
from datetime import datetime
from db_config import get_db

router = APIRouter(prefix="/sensor_nutrientes", tags=["Sensor de Nutrientes"])

# Cria nova medição de sensor de nutrientes
@router.post("/")
def create_sensor_nutriente(valor_fosforo: float, valor_potassio: float, idcultura: int, db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    
    sensor_nutriente = SensorNutrientes(
        valorfosforo=valor_fosforo, valorpotassio=valor_potassio,
        datamedicao=datetime.now(), idcultura=idcultura
    )
    db.add(sensor_nutriente)
    db.commit()
    db.refresh(sensor_nutriente)
    return sensor_nutriente

# Lista medições de sensores de nutrientes
@router.get("/")
def list_sensor_nutrientes(db: Session = Depends(get_db)):
    return db.query(SensorNutrientes).all()