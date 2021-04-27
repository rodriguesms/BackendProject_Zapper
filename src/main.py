from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal, get_db
from .schemas import ApartmentRequest, HouseRequest, LandRequest
from .models import House, Apartment, Land

app = FastAPI()

### CREATE HOUSE

@app.post('/house', status_code=status.HTTP_201_CREATED)
def createHouse(request: HouseRequest, db: Session = Depends(get_db)):
    
    ### CREATING NEW HOUSE OBJECT USING HOUSE SCHEMA ON REQUEST

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

    ### ADDING NEW HOUSE TO DATABASE

    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house

### CREATE APARTMENT

@app.post('/apartment', status_code=status.HTTP_201_CREATED)
def createApartment(request: ApartmentRequest, db: Session = Depends(get_db)):

    ### CREATING NEW APARTMENT OBJECT USING APARTMENT SCHEMA ON REQUEST

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

    ### ADDING NEW APARTMENT TO DATABASE

    db.add(new_apt)
    db.commit()
    db.refresh(new_apt)
    return new_apt

### CREATE LAND

@app.post('/land', status_code=status.HTTP_201_CREATED)
def createLand(request: LandRequest, db: Session = Depends(get_db)):

    ### CREATING NEW LAND OBJECT USING LAND SCHEMA ON REQUEST

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

    ### ADDING NEW LAND TO DATABASE

    db.add(new_land)
    db.commit()
    db.refresh(new_land)
    return new_land

### GET ALL HOUSES

@app.get('/gethouse')
def listHouses(db: Session = Depends(get_db)):

    houses = db.query(House).all() ### GET ALL HOUSES IN HOUSE TABLE FROM DATABASE

    if not houses: ### IF THERE IS NO HOUSE REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"There is no house stored.")

    return houses

### GET ALL APARTMENTS

@app.get('/getapt')
def listApts(db: Session = Depends(get_db)):

    apts = db.query(Apartment).all() ### GET ALL APARTMENTS IN APARTMENT TABLE FROM DATABASE

    if not apts: ### IF THERE IS NO APARTMENT REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"There is no apartment stored.")

    return apts

### GET ALL LANDS

@app.get('/getland')
def listLands(db: Session = Depends(get_db)):

    lands = db.query(Land).all() ### GET ALL LANDS IN LANDS TABLE FROM DATABASE

    if not lands: ### IF THERE IS NO LAND REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"There is no land stored.")

    return lands

### GET HOUSE BY ID

@app.get('/gethouse/{id}', status_code=status.HTTP_302_FOUND)
def showHouse(id, response: Response, db: Session = Depends(get_db)):

    house = db.query(House).filter(House.id == id).first() ### QUERY HOUSE BY ID

    if not house: ### IF HOUSE ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"House with id:{id} id was not found.")

    return house

### GET APARTMENT BY ID

@app.get('/getapt/{id}', status_code=status.HTTP_302_FOUND)
def showApt(id, response: Response, db: Session = Depends(get_db)):

    apt = db.query(Apartment).filter(Apartment.id == id).first() ### QUERY APARTMENT BY ID

    if not apt: ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id:{id} id was not found.")

    return apt

### GET LAND BY ID

@app.get('/getland/{id}', status_code=status.HTTP_302_FOUND)
def showLand(id, response: Response, db: Session = Depends(get_db)):

    land = db.query(Land).filter(Land.id == id).first() ### QUERY LAND BY ID

    if not land: ### IF LAND ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Real estate with id:{id} was not found.")

    return land

### DELETE HOUSE

@app.delete('/house/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteHouse(id, db: Session = Depends(get_db)):

    deletedHouse = db.query(House).filter(House.id == id) ### QUERY HOUSE BY ID
    
    if not deletedHouse.first(): ### IF HOUSE ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"House with id {id} was not found")

    delete(synchronize_session=False) ### DELETING HOUSE
    db.commit() ### COMMIT CHANGES
    return f'The house with id: {id} was deleted'

### DELETE APARTMENT

@app.delete('/apartment/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteApartment(id, db: Session = Depends(get_db)):

    deletedApartment = db.query(Apartment).filter(Apartment.id == id) ### QUERY APARTMENT BY ID

    if not deletedApartment.first(): ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id {id} was not found")

    apt.delete(synchronize_session=False) ### DELETING APARTMENT
    db.commit() ### COMMIT CHANGES
    return f'The Apartment with id: {id} was deleted'

### DELETE LAND

@app.delete('/land/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteLand(id, db: Session = Depends(get_db)): 

    deletedLand = db.query(Land).filter(Land.id == id) ### QUERY LAND BY ID
    
    if not updatedLand.first(): ### IF LAND ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Land with id {id} was not found")

    delete(synchronize_session=False) ###DELETING LAND
    db.commit() ### COMMIT CHANGE
    return f'The real estate with id: {id} was deleted'

### UPDATE HOUSE

@app.put('/house/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateHouse(id, request:HouseRequest, db: Session = Depends(get_db)):

    updatedHouse = db.query(House).filter(House.id == id) ### QUERY BY HOUSE ID

    if not updatedHouse.first(): ### IF HOUSE ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"House with id {id} was not found")

    updatedHouse.update(request) ### UPDATING HOUSE
    db.commit() ### COMMIT CHANGE
    return f'House with {id} updated'

### UPDATE APARTMENT

@app.put('/apartment/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateApartment(id, request:ApartmentRequest, db: Session = Depends(get_db)):

    updatedApartment = db.query(Apartment).filter(Apartment.id == id) ### QUERY BY APARTMENT ID

    if not updatedApartment.first(): ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id {id} was not found")

    updatedHouse.update(request) ### UPDATING APARTMENT
    db.commit() ### COMMIT CHANGE
    return f'Apartment with {id} updated'

### UPDATE LAND

@app.put('/land/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateLand(id, request:LandRequest, db: Session = Depends(get_db)):

    updatedLand = db.query(Land).filter(Land.id == id) ### QUERY BY LAND ID

    if not updatedLand.first(): ### IF LAND ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Land with id {id} was not found")

    updatedLand.update(request) ### UPDATING LAND
    db.commit() ### COMMIT CHANGE
    return f'Land with {id} updated'
