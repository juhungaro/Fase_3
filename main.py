from fastapi import FastAPI
from db_config import engine, Base

from controllers.culturas import router as culturas_router
from controllers.sensor_nutrientes import router as nutrientes_router
from controllers.sensor_phs import router as phs_router
from controllers.sensor_umidades import router as umidades_router

# Cria as tabelas no banco de dados caso não existam
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(culturas_router)
app.include_router(nutrientes_router)
app.include_router(phs_router)
app.include_router(umidades_router)