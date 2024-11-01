from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from db_config import Base


cultura_seq = Sequence("cultura_id_seq", start=1, increment=1)
class Cultura(Base):
    __tablename__ = "culturas"

    idcultura = Column(Integer,
                       cultura_seq, 
                       primary_key=True,
                       server_default=cultura_seq.next_value())
    nome = Column(String(30), unique=True, nullable=False)

    sensores_nutrientes = relationship("SensorNutrientes", back_populates="cultura")
    sensores_ph = relationship("SensorPH", back_populates="cultura")
    sensores_umidades = relationship("SensorUmidades", back_populates="cultura")

nutrientes_seq = Sequence("nutrientes_id_seq", start=1, increment=1)
class SensorNutrientes(Base):
    __tablename__ = "sensor_nutrientes"

    idsensornutriente = Column(Integer,
                       nutrientes_seq, 
                       primary_key=True,
                       server_default=nutrientes_seq.next_value())
    valorfosforo = Column(Float, nullable=False)
    valorpotassio = Column(Float, nullable=False)
    datamedicao = Column(Date, nullable=False)
    idcultura = Column(Integer, ForeignKey("culturas.idcultura"))

    cultura = relationship("Cultura", back_populates="sensores_nutrientes")

ph_seq = Sequence("ph_id_seq", start=1, increment=1)
class SensorPH(Base):
    __tablename__ = "sensor_phs"

    idsensorph = Column(Integer,
                       ph_seq, 
                       primary_key=True,
                       server_default=ph_seq.next_value())
    valor = Column(Float, nullable=False)
    datamedicao = Column(Date, nullable=False)
    idcultura = Column(Integer, ForeignKey("culturas.idcultura"))

    cultura = relationship("Cultura", back_populates="sensores_ph")

umidade_seq = Sequence("umidade_id_seq", start=1, increment=1)
class SensorUmidades(Base):
    __tablename__ = "sensor_umidades"

    idsensorumidade = Column(Integer,
                       umidade_seq, 
                       primary_key=True,
                       server_default=umidade_seq.next_value())
    valor = Column(Float, nullable=False)
    datamedicao = Column(Date, nullable=False)
    idcultura = Column(Integer, ForeignKey("culturas.idcultura"))

    cultura = relationship("Cultura", back_populates="sensores_umidades")