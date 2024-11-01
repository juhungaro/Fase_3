from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SensorUmidades, Cultura
from datetime import datetime
from db_config import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/sensor_umidades", tags=["Sensor de Umidade"])

class SensorUmidadeRequest(BaseModel):
    valor: float
    idcultura: int

# Cria nova medição de sensor de umidade
@router.post("/", summary='Cria nova medição de umidade')
def create_sensor_umidade(sensor: SensorUmidadeRequest = Body(...), db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == sensor.idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    
    sensor_umidade = SensorUmidades(valor=sensor.valor, 
                                    datamedicao=datetime.now(), 
                                    idcultura=sensor.idcultura)
    db.add(sensor_umidade)
    db.commit()
    db.refresh(sensor_umidade)
    return sensor_umidade

# Lista medições de sensores de umidade
@router.get("/", summary='Lista todas as medições de umidade')
def list_sensor_umidades(db: Session = Depends(get_db)):
    return db.query(SensorUmidades).all()