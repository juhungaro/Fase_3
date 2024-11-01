from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SensorPH, Cultura
from datetime import datetime
from db_config import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/sensor_phs", tags=["Sensor de pH"])

class SensorPhRequest(BaseModel):
    valor: float
    idcultura: int

# Cria nova medição de sensor de pH
@router.post("/", summary='Cria nova medição de pH')
def create_sensor_ph(sensor: SensorPhRequest = Body(...), db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == sensor.idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    
    sensor_ph = SensorPH(valor=sensor.valor,
                         datamedicao=datetime.now(),
                         idcultura=sensor.idcultura)
    db.add(sensor_ph)
    db.commit()
    db.refresh(sensor_ph)
    return sensor_ph

# Lista medições de sensores de pH
@router.get("/", summary='Lista todas as medições de pH')
def list_sensor_phs(db: Session = Depends(get_db)):
    return db.query(SensorPH).all()