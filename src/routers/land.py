from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import land

router = APIRouter(
    prefix="/land",
    tags=['Lands']
)

### CREATE LAND

@router.post('/create', status_code=status.HTTP_201_CREATED)
def createLand(request: schemas.LandBase, db: Session = Depends(database.get_db)):
    return land.create(request, db)

### GET ALL LANDS

@router.get('/getall', response_model=List[schemas.responseLand])
def listLands(db: Session = Depends(database.get_db)):
    return land.get_all(db)

### GET LAND BY ID

@router.get('/get/{id}', status_code=200, response_model=schemas.responseLand)
def showLand(id, response: Response, db: Session = Depends(database.get_db)):
    return land.show(id, response, db)

### DELETE LAND

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteLand(id, db: Session = Depends(database.get_db)): 
    return land.delete(id, db)

### UPDATE LAND

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateLand(id, request:schemas.LandBase, db: Session = Depends(database.get_db)):
    return land.update(id, request, db)
