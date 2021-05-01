from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from . import database, schemas, models
from .hashing import Hash
from typing import List

app = FastAPI()

models.Base.metadata.create_all(database.engine) ### DINAMICALLY UPDATING DATABASE WITH NEW MODELS

get_db = database.get_db

### CREATE USER

@app.post('/user', status_code=status.HTTP_201_CREATED, tags=['users'])
def createUser(request: schemas.userRequest, db: Session = Depends(get_db)):

    ### CREATING NEW USER OBJECT USING USER SCHEMA ON REQUEST

    new_user = models.User(
        name = request.name,
        email = request.email,
        password = Hash.bcrypt(request.password) ### HASHING PASSWORD
    )

    ### ADDING NEW USER TO DATABASE

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


### CREATE HOUSE

@app.post('/house', status_code=status.HTTP_201_CREATED, tags=['houses'])
def createHouse(request: schemas.House, db: Session = Depends(get_db)):
    
    ### CREATING NEW HOUSE OBJECT USING HOUSE SCHEMA ON REQUEST

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

    ### ADDING NEW HOUSE TO DATABASE

    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house

### CREATE APARTMENT

@app.post('/apartment', status_code=status.HTTP_201_CREATED, tags=['apartments'])
def createApartment(request: schemas.ApartmentRequest, db: Session = Depends(get_db)):

    ### CREATING NEW APARTMENT OBJECT USING APARTMENT SCHEMA ON REQUEST

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

    ### ADDING NEW APARTMENT TO DATABASE

    db.add(new_apt)
    db.commit()
    db.refresh(new_apt)
    return new_apt

### CREATE LAND

@app.post('/land', status_code=status.HTTP_201_CREATED, tags=['lands'])
def createLand(request: schemas.LandRequest, db: Session = Depends(get_db)):

    ### CREATING NEW LAND OBJECT USING LAND SCHEMA ON REQUEST

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

    ### ADDING NEW LAND TO DATABASE

    db.add(new_land)
    db.commit()
    db.refresh(new_land)
    return new_land

### GET ALL USERS

@app.get('/getuser', response_model=List[schemas.responseUser], tags=['users'])
def listUsers(db: Session = Depends(get_db)):
    
    users = db.query(models.User).all() ### GET ALL USERS IN USER TABLE FROM DATABASE

    if not users: ### IF THERE IS NO USER REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="There is no user registered.")

    return users


### GET ALL HOUSES

@app.get('/gethouse', response_model=List[schemas.responseHouse], tags=['houses'])
def listHouses(db: Session = Depends(get_db)):

    houses = db.query(models.House).all() ### GET ALL HOUSES IN HOUSE TABLE FROM DATABASE

    if not houses: ### IF THERE IS NO HOUSE REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="There is no house stored.")

    return houses

### GET ALL APARTMENTS

@app.get('/getapt', response_model=List[schemas.responseApartment], tags=['apartments'])
def listApts(db: Session = Depends(get_db)):

    apts = db.query(models.Apartment).all() ### GET ALL APARTMENTS IN APARTMENT TABLE FROM DATABASE

    if not apts: ### IF THERE IS NO APARTMENT REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="There is no apartment stored.")

    return apts

### GET ALL LANDS

@app.get('/getland', response_model=List[schemas.responseLand], tags=['lands'])
def listLands(db: Session = Depends(get_db)):

    lands = db.query(models.Land).all() ### GET ALL LANDS IN LANDS TABLE FROM DATABASE

    if not lands: ### IF THERE IS NO LAND REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="There is no land stored.")

    return lands

### GET USER BY ID

@app.get('/getuser/{id}', status_code=200, response_model=schemas.responseUser, tags=['users'])
def showUser(id, response: Response, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first() ### QUERY USER BY ID

    if not user: ### IF USER ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id:{id} was not found")

    return user

### GET HOUSE BY ID

@app.get('/gethouse/{id}', status_code=200, response_model=schemas.responseHouse, tags=['houses'])
def showHouse(id, response: Response, db: Session = Depends(get_db)):

    house = db.query(models.House).filter(models.House.id == id).first() ### QUERY HOUSE BY ID

    if not house: ### IF HOUSE ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"House with id:{id} id was not found.")

    return house

### GET APARTMENT BY ID

@app.get('/getapt/{id}', status_code=200,response_model=schemas.responseApartment, tags=['apartments'])
def showApt(id, response: Response, db: Session = Depends(get_db)):

    apt = db.query(models.Apartment).filter(models.Apartment.id == id).first() ### QUERY APARTMENT BY ID

    if not apt: ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id:{id} id was not found.")

    return apt

### GET LAND BY ID

@app.get('/getland/{id}', status_code=200, response_model=schemas.responseLand, tags=['lands'])
def showLand(id, response: Response, db: Session = Depends(get_db)):

    land = db.query(models.Land).filter(models.Land.id == id).first() ### QUERY LAND BY ID

    if not land: ### IF LAND ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Real estate with id:{id} was not found.")

    return land

### DELETE HOUSE

@app.delete('/deletehouse/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['houses'])
def deleteHouse(id, db: Session = Depends(get_db)):

    db.query(models.House).filter(models.House.id == id).delete(synchronize_session=False)
    db.commit()
    return f"The House with id {id} was deleted"


### DELETE APARTMENT

@app.delete('/apartment/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['apartments'])
def deleteApartment(id, db: Session = Depends(get_db)):

    deletedApartment = db.query(models.Apartment).filter(models.Apartment.id == id) ### QUERY APARTMENT BY ID

    if not deletedApartment.first(): ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id {id} was not found")

    deletedApartment.delete(synchronize_session=False) ### DELETING APARTMENT
    db.commit() ### COMMIT CHANGES
    return f'The Apartment with id: {id} was deleted'

### DELETE LAND

@app.delete('/land/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['lands'])
def deleteLand(id, db: Session = Depends(get_db)): 

    deletedLand = db.query(models.Land).filter(models.Land.id == id) ### QUERY LAND BY ID
    
    if not deletedLand.first(): ### IF LAND ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Land with id {id} was not found")

    deletedLand.delete(synchronize_session=False) ###DELETING LAND
    db.commit() ### COMMIT CHANGE
    return f'The real estate with id: {id} was deleted'

### UPDATE HOUSE

@app.put('/updateHouse/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['houses'])
def updateHouse(id, request: schemas.House, db: Session = Depends(get_db)):
    
    house = db.query(models.House).filter(models.House.id == id) ### QUERY BI HOUSE ID
    
    if not house.first(): ### IF HOUSE ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"House with id {id} was not found")

    house.update({
        "title": request.title,
        "zip_code": request.zip_code,
        "city": request.city,
        "neighborhood": request.neighborhood,
        "street": request.street,
        "number": request.number,
        "floor_quant": request.floor_quant,
        "rooms": request.rooms,
        "land_area": request.land_area,
        "area": request.area,
        "definition": request.definition,
        "price": request.price
    })


    db.commit()
    return f"House with id {id} was updated"

### UPDATE APARTMENT

@app.put('/apartment/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['apartments'])
def updateApartment(id, request:schemas.ApartmentRequest, db: Session = Depends(get_db)):

    apartment = db.query(models.Apartment).filter(models.Apartment.id == id) ### QUERY BY APARTMENT ID

    if not apartment.first(): ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id {id} was not found")

    apartment.update({ ### UPDATING APARTMENT
        "title" : request.title, 
        "zip_code" : request.zip_code, 
        "city" : request.city, 
        "neighborhood" : request.neighborhood, 
        "street" : request.street, 
        "number" : request.number, 
        "definition" : request.definition,
        "area"  : request.area,
        "condom_value" : request.condom_value,
        "rooms" : request.rooms, 
        "floor" : request.floor,
        "garage_spots" : request.garage_spots,
        "sun_position" : request.sun_position,
        "price" : request.price
    }) 

    db.commit() ### COMMIT CHANGE
    return f'Apartment with id {id} updated'

### UPDATE LAND

@app.put('/land/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['lands'])
def updateLand(id, request:schemas.LandRequest, db: Session = Depends(get_db)):

    land = db.query(models.Land).filter(models.Land.id == id) ### QUERY BY LAND ID

    if not land.first(): ### IF LAND ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Land with id {id} was not found")

    land.update({
        "title" : request.title, 
        "zip_code" : request.zip_code, 
        "city" : request.city, 
        "neighborhood" : request.neighborhood, 
        "street" : request.street, 
        "number" : request.number, 
        "definition" : request.definition,
        "area"  : request.area,
        "price" : request.price
    }) ### UPDATING LAND
    db.commit() ### COMMIT CHANGE
    return f'Land with id {id} updated'
