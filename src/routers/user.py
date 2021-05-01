from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models, hashing
from sqlalchemy.orm import Session


router = APIRouter()

### CREATE USER

@router.post('/user', status_code=status.HTTP_201_CREATED, tags=['users'])
def createUser(request: schemas.User, db: Session = Depends(database.get_db)):

    ### CREATING NEW USER OBJECT USING USER SCHEMA ON REQUEST

    new_user = models.User(
        name = request.name,
        email = request.email,
        password = hashing.Hash.bcrypt(request.password) ### HASHING PASSWORD
    )

    ### ADDING NEW USER TO DATABASE

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

### GET ALL USERS

@router.get('/getuser', response_model=List[schemas.ShowUser], tags=['users'])
def listUsers(db: Session = Depends(database.get_db)):
    
    users = db.query(models.User).all() ### GET ALL USERS IN USER TABLE FROM DATABASE

    if not users: ### IF THERE IS NO USER REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="There is no user registered.")

    return users

### GET USER BY ID

@router.get('/getuser/{id}', status_code=200, response_model=schemas.ShowUser, tags=['users'])
def showUser(id, response: Response, db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.id == id).first() ### QUERY USER BY ID

    if not user: ### IF USER ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id:{id} was not found")

    return user