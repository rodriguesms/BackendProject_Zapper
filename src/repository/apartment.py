from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, HTTPException
from .. import models, schemas, database

def create(request: schemas.ApartmentBase, db: Session = Depends(database.get_db)):

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
        price = request.price,
        owner_id = 1
    )

    ### ADDING NEW APARTMENT TO DATABASE

    db.add(new_apt)
    db.commit()
    db.refresh(new_apt)
    return new_apt

def get_all(db: Session = Depends(database.get_db)):

    apts = db.query(models.Apartment).all() ### GET ALL APARTMENTS IN APARTMENT TABLE FROM DATABASE

    if not apts: ### IF THERE IS NO APARTMENT REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="There is no apartment stored.")

    return apts

def show(id, response: Response, db: Session = Depends(database.get_db)):

    apt = db.query(models.Apartment).filter(models.Apartment.id == id).first() ### QUERY APARTMENT BY ID

    if not apt: ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id:{id} id was not found.")

    return apt

def delete(id, db: Session = Depends(database.get_db)):

    apt = db.query(models.Apartment).filter(models.Apartment.id == id) ### QUERY APARTMENT BY ID

    if not apt.first(): ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id {id} was not found")

    apt.delete(synchronize_session=False) ### DELETING APARTMENT
    db.commit() ### COMMIT CHANGES
    return f'The Apartment with id: {id} was deleted'

def update(id, request:schemas.ApartmentBase, db: Session = Depends(database.get_db)):

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