from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models
from .database import engine, SessionLocal, get_db
from .schemas import CreateApartmentRequest, CreateHouseRequest, CreateLandRequest

app = FastAPI()

@app.post('/addhouse', status_code=status.HTTP_201_CREATED)
def createHouse(request: CreateHouseRequest, db: Session = Depends(get_db)):
    new_house = models.House(
        title = request.title, 
        zip_code = request.zip_code, 
        city = request.city, 
        neighborhood = request.neighborhood, 
        street = request.street, 
        number = request.number, 
        floor_quant = request.floor_quant, 
        rooms = request.rooms, 
        land_area = request.land_area, 
        area  = request.area, 
        definition = request.definition, 
        price = request.price
    )
    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house


@app.post('/addapartment', status_code=status.HTTP_201_CREATED)
def createApartment(request: schemas.CreateApartmentRequest, db: Session = Depends(get_db)):
    new_apt = models.Apartment(
        title = request.title, 
        zip_code = request.zip_code, 
        city = request.city, 
        neighborhood = request.neighborhood, 
        street = request.street, 
        number = request.number, 
        definition = request.definition,
        area  = request.area,
        condom_value = request.condom_value,
        rooms = request.rooms, 
        floor = request.floor,
        garage_spots = request.garage_spots,
        sun_position = request.sun_position,
        price = request.price
    )
    db.add(new_apt)
    db.commit()
    db.refresh(new_apt)
    return new_apt

@app.post('/addland', status_code=status.HTTP_201_CREATED)
def createApartment(request: schemas.CreateLandRequest, db: Session = Depends(get_db)):
    new_land = models.Land(
        title = request.title, 
        zip_code = request.zip_code, 
        city = request.city, 
        neighborhood = request.neighborhood, 
        street = request.street, 
        number = request.number, 
        definition = request.definition,
        area  = request.area,
        price = request.price
    )
    db.add(new_land)
    db.commit()
    return new_land