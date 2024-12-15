#!/usr/bin/env python3
"""
python
"""
from pymongo import MongoClient
"""
pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """_summary_

    Args:
        mongo_collection: coleccion de la BD

    Returns:
        int: id del dato insertado
    """
    inserted = mongo_collection.insert_one(kwargs)
    
    return inserted.inserted_id
