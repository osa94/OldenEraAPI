from fastapi import FastAPI
from routers.units import router as units_router


app = FastAPI()
app.include_router(units_router)

