from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import apartment

router = APIRouter(
    prefix="/apartment",
    tags=['Apartments']
)

### CREATE APARTMENT

@router.post('/create', status_code=status.HTTP_201_CREATED)
def createApartment(request: schemas.ApartmentBase, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return apartment.create(request, db)

### GET ALL APARTMENTS

@router.get('/getall', response_model=List[schemas.responseApartment])
def listApts(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return apartment.get_all(db)

### GET APARTMENT BY ID

@router.get('/get/{id}', status_code=200,response_model=schemas.responseApartment)
def showApt(id, response: Response, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return apartment.show(id, response, db)

### DELETE APARTMENT

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteApartment(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return apartment.delete(id, db)

### UPDATE APARTMENT

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateApartment(id, request:schemas.ApartmentBase, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return apartment.update(id, request, db)