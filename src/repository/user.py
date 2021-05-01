from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, HTTPException
from .. import models, schemas, database

def create(request: schemas.User, db: Session = Depends(database.get_db)):

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

def get_all(db: Session = Depends(database.get_db)):
    
    users = db.query(models.User).all() ### GET ALL USERS IN USER TABLE FROM DATABASE

    if not users: ### IF THERE IS NO USER REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="There is no user registered.")

    return users

def show(id, response: Response, db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.id == id).first() ### QUERY USER BY ID

    if not user: ### IF USER ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id:{id} was not found")

    return user