#!/usr/bin/python3
"""Amenity Module for HBNB project"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity  # Import the place_amenity table
from models.base_model import Base
from models.place import place_amenity

class Amenity(BaseModel, Base):
    """The Amenity class, contains amenity name"""
    __tablename__ = "amenities"  # Represents the table name in the database

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary=place_amenity, back_populates="amenities")
