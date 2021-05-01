from typing import List
from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/apartment",
    tags=['Apartments']
)

### CREATE APARTMENT

@router.post('/create', status_code=status.HTTP_201_CREATED)
def createApartment(request: schemas.ApartmentBase, db: Session = Depends(database.get_db)):

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

### GET ALL APARTMENTS

@router.get('/getall', response_model=List[schemas.responseApartment])
def listApts(db: Session = Depends(database.get_db)):

    apts = db.query(models.Apartment).all() ### GET ALL APARTMENTS IN APARTMENT TABLE FROM DATABASE

    if not apts: ### IF THERE IS NO APARTMENT REGISTERED: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail="There is no apartment stored.")

    return apts

### GET APARTMENT BY ID

@router.get('/get/{id}', status_code=200,response_model=schemas.responseApartment)
def showApt(id, response: Response, db: Session = Depends(database.get_db)):

    apt = db.query(models.Apartment).filter(models.Apartment.id == id).first() ### QUERY APARTMENT BY ID

    if not apt: ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id:{id} id was not found.")

    return apt

### DELETE APARTMENT

@router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteApartment(id, db: Session = Depends(database.get_db)):

    deletedApartment = db.query(models.Apartment).filter(models.Apartment.id == id) ### QUERY APARTMENT BY ID

    if not deletedApartment.first(): ### IF APARTMENT ID WAS NOT FOUND: RAISE EXCEPTION
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Apartment with id {id} was not found")

    deletedApartment.delete(synchronize_session=False) ### DELETING APARTMENT
    db.commit() ### COMMIT CHANGES
    return f'The Apartment with id: {id} was deleted'

### UPDATE APARTMENT

@router.put('/update/{id}', status_code=status.HTTP_202_ACCEPTED)
def updateApartment(id, request:schemas.ApartmentBase, db: Session = Depends(database.get_db)):

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