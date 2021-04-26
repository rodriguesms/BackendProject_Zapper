from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db
from .schemas import CreateApartmentRequest, CreateHouseRequest, CreateLandRequest
from .models import House, Apartment, Land

app = FastAPI()

@app.post('/addhouse', status_code=status.HTTP_201_CREATED)
def createHouse(request: CreateHouseRequest, db: Session = Depends(get_db)):
    new_house = House(
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
def createApartment(request: CreateApartmentRequest, db: Session = Depends(get_db)):
    new_apt = Apartment(
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
def createApartment(request: CreateLandRequest, db: Session = Depends(get_db)):
    new_land = Land(
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

@app.get('/gethouse')
def listHouses(db: Session = Depends(get_db)):
    houses = db.query(House).all()
    if not houses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no house stored.")
    return houses

@app.get('/getapt')
def listApts(db: Session = Depends(get_db)):
    apts = db.query(Apartment).all()
    if not apts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no apartment stored.")
    return apts

@app.get('/getland')
def listLands(db: Session = Depends(get_db)):
    lands = db.query(Land).all()
    if not lands:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no land stored.")
    return lands

@app.get('/gethouse/{id}', status_code=status.HTTP_302_FOUND)
def showHouse(id, response: Response, db: Session = Depends(get_db)):
    house = db.query(House).filter(House.id == id).first()
    if not house:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"House with {id} id was not found.")
    return house

@app.get('/getapt/{id}', status_code=status.HTTP_302_FOUND)
def showApt(id, response: Response, db: Session = Depends(get_db)):
    apt = db.query(Apartment).filter(Apartment.id == id).first()
    if not apt:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Apartment with {id} id was not found.")
    return apt

@app.get('/getland/{id}', status_code=status.HTTP_302_FOUND)
def showLand(id, response: Response, db: Session = Depends(get_db)):
    land = db.query(Land).filter(Land.id == id).first()
    if not land:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Real estate with {id} id was not found.")
    return land