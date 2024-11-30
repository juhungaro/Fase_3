from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from models import Sensor, Cultura
from datetime import datetime
from db_config import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/sensores", tags=["Dados de Sensores"])

class SensorRequest(BaseModel):
    valor_fosforo: float
    valor_potassio: float
    valor_ph: float
    valor_umidade: float
    valor_temperatura: float
    precipitacao: float
    irrigador_ligado: bool
    idcultura: int

# Cria nova medição de sensor
@router.post("/", summary='Cria nova medição de nutrientes, ph, temperatura e umidade')
def create_sensor(sensor: SensorRequest = Body(...), db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == sensor.idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    
    sensor = Sensor(
        valorfosforo=sensor.valor_fosforo, 
        valorpotassio=sensor.valor_potassio,
        valorph = sensor.valor_ph,
        valorumidade = sensor.valor_umidade,
        valortemperatura = sensor.valor_temperatura,
        irrigadorligado = sensor.irrigador_ligado,
        precipitacao = sensor.precipitacao,
        datamedicao=datetime.now(),
        idcultura=sensor.idcultura)
    
    db.add(sensor)
    db.commit()
    db.refresh(sensor)
    return {"idsensor": sensor.idsensor}

# Lista medições de sensores
@router.get("/", summary='Lista todas as medições')
def list_sensor(db: Session = Depends(get_db)):
    return db.query(Sensor).all()