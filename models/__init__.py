#!/usr/bin/python3
"""
initialize the program package
"""
from os import getenv

storage_t = getenv("DATA_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

