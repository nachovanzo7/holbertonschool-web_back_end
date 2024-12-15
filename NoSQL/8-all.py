#!/usr/bin/env python3
"""
python
"""
from pymongo import MongoClient
"""
pymongo
"""


def list_all(mongo_collection):
    """

    Args:
        mongo_collection: coleccion de mi BD
    """    
    if (mongo_collection.count_documents({}) == 0):
        return []
    
    lista = list(mongo_collection.find())
    return lista
