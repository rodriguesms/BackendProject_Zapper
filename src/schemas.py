from pydantic import BaseModel

class userRequest(BaseModel):
    name: str
    email: str
    password: str

class HouseRequest(BaseModel):
    title: str
    zip_code: str
    city: str
    neighborhood: str
    street: str
    number: int
    floor_quant: int
    rooms: int
    land_area: float
    area: float
    definition: bool
    price: float

class responseHouse(BaseModel):
    title: str

    class Config():
        orm_mode = True

class ApartmentRequest(BaseModel):
    title: str
    zip_code: str
    city: str
    neighborhood: str
    street: str
    number: int
    definition: bool
    area: float
    condom_value: float
    rooms: int
    floor: int
    garage_spots: int
    sun_position: str
    price: float

class responseApartment(BaseModel):
    title: str

    class Config():
        orm_mode = True

class LandRequest(BaseModel):
    title: str
    zip_code: str
    city: str
    neighborhood: str
    street: str
    number: int
    definition: bool
    area: float
    price: float

class responseLand(BaseModel):
    title: str

    class Config():
        orm_mode = True