from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter()

### CREATE LAND

@router.post('/land', status_code=status.HTTP_201_CREATED, tags=['lands'])
def createLand(request: schemas.LandBase, db: Session = Depends(database.get_db)):

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
        price = request.price,
        owner_id = 1    
    )

    ### ADDING NEW LAND TO DATABASE

    db.add(new_land)
    db.commit()
    db.refresh(new_land)
    return new_land

### GET ALL LANDS

@router.get('/getland', response_model=List[schemas.responseLand], tags=['lands'])
def listLands(db: Session = Depends(database.get_db)):

    lands = db.query(models.Land).all() ### GET ALL LANDS IN LANDS TABLE FROM DATABASE

    if not lands: ### IF THERE IS NO LAND REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="There is no land stored.")

    return lands

### GET LAND BY ID

@router.get('/getland/{id}', status_code=200, response_model=schemas.responseLand, tags=['lands'])
def showLand(id, response: Response, db: Session = Depends(database.get_db)):

    land = db.query(models.Land).filter(models.Land.id == id).first() ### QUERY LAND BY ID

    if not land: ### IF LAND ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Real estate with id:{id} was not found.")

    return land



### DELETE LAND

@router.delete('/land/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['lands'])
def deleteLand(id, db: Session = Depends(database.get_db)): 

    deletedLand = db.query(models.Land).filter(models.Land.id == id) ### QUERY LAND BY ID
    
    if not deletedLand.first(): ### IF LAND ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Land with id {id} was not found")

    deletedLand.delete(synchronize_session=False) ###DELETING LAND
    db.commit() ### COMMIT CHANGE
    return f'The real estate with id: {id} was deleted'


### UPDATE LAND

@router.put('/land/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['lands'])
def updateLand(id, request:schemas.LandBase, db: Session = Depends(database.get_db)):

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
