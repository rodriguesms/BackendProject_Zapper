from pydantic import BaseModel
from typing import List

class userBase(BaseModel):
    name: str
    email: str
    password: str

class HouseBase(BaseModel):
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

class ApartmentBase(BaseModel):
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

class LandBase(BaseModel):
    title: str
    zip_code: str
    city: str
    neighborhood: str
    street: str
    number: int
    definition: bool
    area: float
    price: float

class House(HouseBase):
    class Config():
        orm_mode = True

class Apartment(ApartmentBase):
    class Config():
        orm_mode = True

class Land(LandBase):
    class Config():
        orm_mode = True

class responseUser(BaseModel):
    name: str
    email: str
    houses: List[House] = []
    apartments: List[Apartment] = []
    lands: List[Land] = []
    class Config():
        orm_mode = True

class responseHouse(BaseModel):
    title: str
    announcer: responseUser
    class Config():
        orm_mode = True

class responseApartment(BaseModel):
    title: str
    announcer: responseUser
    class Config():
        orm_mode = True

class responseLand(BaseModel):
    title: str
    announcer: responseUser
    class Config():
        orm_mode = True