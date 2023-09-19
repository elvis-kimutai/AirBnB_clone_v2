#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

# Import the necessary storage classes
if "HBNB_TYPE_STORAGE" in os.environ and os.environ["HBNB_TYPE_STORAGE"] == "db":

    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
