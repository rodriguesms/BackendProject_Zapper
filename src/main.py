from fastapi import FastAPI
from . import database, models
from .routers import house, land, user, apartment

app = FastAPI()
models.Base.metadata.create_all(database.engine) ### DINAMICALLY UPDATING DATABASE WITH NEW MODELS
get_db = database.get_db

app.include_router(house.router)
app.include_router(user.router)
app.include_router(apartment.router)
app.include_router(land.router)