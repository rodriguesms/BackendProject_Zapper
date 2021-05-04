from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
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

class House(HouseBase):
    class Config():
        orm_mode = True

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

class Apartment(ApartmentBase):
    class Config():
        orm_mode = True

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

class Land(LandBase):
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    houses: List[House] = []
    apartments: List[Apartment] = []
    lands: List[Land] = []
    class Config():
        orm_mode = True

class ShowUserPersonalInfo(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True

class responseHouse(BaseModel):
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
    owner: ShowUserPersonalInfo

    class Config():
        orm_mode = True



class responseApartment(BaseModel):
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
    owner: ShowUserPersonalInfo

    class Config():
        orm_mode = True

class responseLand(BaseModel):
    title: str
    zip_code: str
    city: str
    neighborhood: str
    street: str
    number: int
    definition: bool
    area: float
    price: float
    owner:ShowUserPersonalInfo

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None