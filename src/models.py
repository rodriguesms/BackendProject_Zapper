from sqlalchemy import Integer, String, Float, Boolean
from .database import Base
from sqlalchemy.sql.schema import Column

class House(Base):
    __tablename__ = 'Houses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    neighborhood = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(Integer)
    floor_quant = Column(Integer, nullable=False)
    rooms = Column(Integer)
    land_area = Column(Float, nullable=False)
    area = Column(Float, nullable=False)
    definition = Column(Boolean, nullable=False)
    price = Column(Float, nullable=False)

class Apartment(Base):
    __tablename__ = 'Apartments'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    neighborhood = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(Integer)
    definition = Column(Boolean, nullable=False)
    area = Column(Float, nullable=False)
    condom_value = Column(Float, nullable=False)
    rooms = Column(Integer)
    floor = Column(Integer, nullable=False)
    garage_spots = Column(Integer)
    sun_position = Column(String)
    price = Column(Float, nullable=False)

class Land(Base):
    __tablename__ = 'Lands'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    city = Column(String, nullable=False)
    neighborhood = Column(String, nullable=False)
    street = Column(String, nullable=False)
    number = Column(Integer)
    definition = Column(Boolean, nullable=False)
    area = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
