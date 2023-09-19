#!/usr/bin/python3
"""State Module for HBNB project"""
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel):
    """The state class, contains name"""
    __tablename__ = "states"  # Represents the table name in the database

    name = Column(String(128), nullable=False)  # Column for state name

    # For DBStorage
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    # For FileStorage
    @property
    def cities(self):
        """Getter attribute to return list of City instances with matching state_id"""
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
