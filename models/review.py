#!/usr/bin/python3
"""Review Module for HBNB project"""
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base

class Review(BaseModel, Base):
    """A review of a place"""
    __tablename__ = "reviews"

    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
