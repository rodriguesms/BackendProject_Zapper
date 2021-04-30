from sqlalchemy import Integer, String, Float, Boolean, ForeignKey
from .database import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    houses = relationship('House', back_populates="announcer")
    apartments = relationship('Apartment', back_populates="announcer")
    lands = relationship('Land', back_populates="announcer")

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
    user_id = Column(Integer, ForeignKey('Users.id'))

    announcer = relationship("User", back_populates="houses")

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
    user_id = Column(Integer, ForeignKey('Users.id'))

    announcer = relationship("User", back_populates="apartments")


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
    user_id = Column(Integer, ForeignKey('Users.id'))

    announcer = relationship("User", back_populates="lands")

