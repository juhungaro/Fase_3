from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import SensorUmidades, Cultura
from datetime import datetime
from db_config import get_db

router = APIRouter(prefix="/sensor_umidades", tags=["Sensor de Umidade"])

# Cria nova medição de sensor de umidade
@router.post("/")
def create_sensor_umidade(valor: float, idcultura: int, db: Session = Depends(get_db)):
    cultura = db.query(Cultura).filter(Cultura.idcultura == idcultura).first()
    if cultura is None:
        raise HTTPException(status_code=404, detail="Cultura não encontrada")
    
    sensor_umidade = SensorUmidades(valor=valor, 
                                    datamedicao=datetime.now(), 
                                    idcultura=idcultura)
    db.add(sensor_umidade)
    db.commit()
    db.refresh(sensor_umidade)
    return sensor_umidade

# Lista medições de sensores de umidade
@router.get("/")
def list_sensor_umidades(db: Session = Depends(get_db)):
    return db.query(SensorUmidades).all()