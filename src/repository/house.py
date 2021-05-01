from sqlalchemy.orm import Session
from fastapi import Depends, Response, status, HTTPException
from .. import models, schemas, database

def get_all(db : Session):
    houses = db.query(models.House).all() ### GET ALL HOUSES IN HOUSE TABLE FROM DATABASE

    if not houses: ### IF THERE IS NO HOUSE REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="There is no house stored.")

    return houses

def create(request: schemas.HouseBase, db: Session = Depends(database.get_db)):
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

def show(id: int, response: Response, db: Session = Depends(database.get_db)):

    house = db.query(models.House).filter(models.House.id == id).first() ### QUERY HOUSE BY ID

    if not house: ### IF HOUSE ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"House with id:{id} id was not found.")

    return house

def delete(id, db: Session = Depends(database.get_db)):

    house = db.query(models.House).filter(models.House.id == id)
    
    if not house.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"House with id:{id} id was not found.")

    house.delete(synchronize_session=False)
    db.commit()
    return f"The House with id {id} was deleted"

def update(id, request: schemas.HouseBase, db: Session = Depends(database.get_db)):
    
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