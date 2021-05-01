from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter()

### GET ALL HOUSES

@router.get('/gethouse', response_model=List[schemas.responseHouse], tags=['houses'])
def listHouses(db: Session = Depends(database.get_db)):

    houses = db.query(models.House).all() ### GET ALL HOUSES IN HOUSE TABLE FROM DATABASE

    if not houses: ### IF THERE IS NO HOUSE REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="There is no house stored.")

    return houses

### CREATE HOUSE

@router.post('/house', status_code=status.HTTP_201_CREATED, tags=['houses'])
def createHouse(request: schemas.HouseBase, db: Session = Depends(database.get_db)):
    
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
        price = request.price,
        owner_id = 1
    )

    ### ADDING NEW HOUSE TO DATABASE

    db.add(new_house)
    db.commit()
    db.refresh(new_house)
    return new_house

### GET HOUSE BY ID

@router.get('/gethouse/{id}', status_code=200, response_model=schemas.responseHouse, tags=['houses'])
def showHouse(id, response: Response, db: Session = Depends(database.get_db)):

    house = db.query(models.House).filter(models.House.id == id).first() ### QUERY HOUSE BY ID

    if not house: ### IF HOUSE ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"House with id:{id} id was not found.")

    return house

### DELETE HOUSE

@router.delete('/deletehouse/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['houses'])
def deleteHouse(id, db: Session = Depends(database.get_db)):

    db.query(models.House).filter(models.House.id == id).delete(synchronize_session=False)
    db.commit()
    return f"The House with id {id} was deleted"

### UPDATE HOUSE

@router.put('/updateHouse/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['houses'])
def updateHouse(id, request: schemas.HouseBase, db: Session = Depends(database.get_db)):
    
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