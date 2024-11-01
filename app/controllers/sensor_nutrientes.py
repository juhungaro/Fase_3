from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from models import SensorNutrientes, Cultura
from datetime import datetime
from db_config import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/sensor_nutrientes", tags=["Sensor de Nutrientes"])

class SensorNutrienteRequest(BaseModel):
    valor_fosforo: float
    valor_potassio: float
    idcultura: int

# Cria nova medição de sensor de nutrientes
@router.post("/", summary='Cria nova medição de nutrientes')
def create_sensor_nutriente(sensor: SensorNutrienteRequest = Body(...), db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == sensor.idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    
    sensor_nutriente = SensorNutrientes(valorfosforo=sensor.valor_fosforo, 
                                        valorpotassio=sensor.valor_potassio,
                                        datamedicao=datetime.now(),
                                        idcultura=sensor.idcultura)
    db.add(sensor_nutriente)
    db.commit()
    db.refresh(sensor_nutriente)
    return sensor_nutriente

# Lista medições de sensores de nutrientes
@router.get("/", summary='Lista todas as medições de nutrientes')
def list_sensor_nutrientes(db: Session = Depends(get_db)):
    return db.query(SensorNutrientes).all()