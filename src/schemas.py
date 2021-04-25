from pydantic import BaseModel

class CreateHouseRequest(BaseModel):
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

class CreateApartmentRequest(BaseModel):
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

class CreateLandRequest(BaseModel):
    title: str
    zip_code: str
    city: str
    neighborhood: str
    street: str
    number: int
    definition: bool
    area: float
    price: float