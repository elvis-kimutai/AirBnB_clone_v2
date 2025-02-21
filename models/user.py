#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # one-to-many relationship with Place
    places = relationship("Place", backref="user", cascade="all, delete-orphan")

    # one-to-many relationship with Review
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
