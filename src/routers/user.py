from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models, hashing
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

### CREATE USER

@router.post('/create', status_code=status.HTTP_201_CREATED)
def createUser(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)

### GET ALL USERS

@router.get('/getall', response_model=List[schemas.ShowUser])
def listUsers(db: Session = Depends(database.get_db)):
    return user.get_all(db)

### GET USER BY ID

@router.get('/get/{id}', status_code=200, response_model=schemas.ShowUser)
def showUser(id, response: Response, db: Session = Depends(database.get_db)):
    return user.show(id, response, db)