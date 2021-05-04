from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import house

router = APIRouter(
    prefix="/house",
    tags=['Houses']
)

### GET ALL HOUSES

@router.get('/getall', response_model=List[schemas.responseHouse])
def listHouses(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return house.get_all(db)

### CREATE HOUSE

@router.post('/create', status_code=status.HTTP_201_CREATED)
def createHouse(request: schemas.HouseBase, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return house.create(request, db)

### GET HOUSE BY ID

@router.get('/get/{id}', status_code=200, response_model=schemas.responseHouse)
def showHouse(id, response: Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return house.show(id, response, db)

### DELETE HOUSE

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteHouse(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return house.delete(id, db)

### UPDATE HOUSE

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateHouse(id, request: schemas.HouseBase, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return house.update(id, request, db)