from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SensorPH, Cultura
from datetime import datetime
from db_config import get_db

router = APIRouter(prefix="/sensor_phs", tags=["Sensor de pH"])

# Cria nova medição de sensor de pH
@router.post("/")
def create_sensor_ph(valor: float, idcultura: int, db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    
    sensor_ph = SensorPH(valor=valor, datamedicao=datetime.now(), idcultura=idcultura)
    db.add(sensor_ph)
    db.commit()
    db.refresh(sensor_ph)
    return sensor_ph

# Lista medições de sensores de pH
@router.get("/")
def list_sensor_phs(db: Session = Depends(get_db)):
    return db.query(SensorPH).all()