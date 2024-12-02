from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Sequence, Boolean
from sqlalchemy.orm import relationship
from db_config import Base

# Tabela Culturas
cultura_seq = Sequence("cultura_id_seq", start=1, increment=1) # Oracle precisa dessa classe para a incrementação da primary key funcionar corretamente
class Cultura(Base):
    __tablename__ = "culturas"

    idcultura = Column(Integer,
                       cultura_seq, 
                       primary_key=True,
                       server_default=cultura_seq.next_value())
    nome = Column(String(30), unique=True, nullable=False)

    sensores = relationship("Sensor", back_populates="cultura")

# Tabela Sensores
sensor_seq = Sequence("sensor_id_seq", start=1, increment=1)
class Sensor(Base):
    __tablename__ = "sensores"

    idsensor = Column(Integer,
                       sensor_seq, 
                       primary_key=True,
                       server_default=sensor_seq.next_value())
    valorfosforo = Column(Float, nullable=False)
    valorpotassio = Column(Float, nullable=False)
    valorph = Column(Float, nullable=False)
    valorumidade = Column(Float, nullable=False)
    valortemperatura = Column(Float, nullable=False)
    precipitacao = Column(Float, nullable=False)
    irrigadorligado = Column(Boolean, nullable=False)
    datamedicao = Column(DateTime, nullable=False)
    idcultura = Column(Integer, ForeignKey("culturas.idcultura"))

    cultura = relationship("Cultura", back_populates="sensores")