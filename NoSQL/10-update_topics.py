#!/usr/bin/env python3
"""
python
"""
from pymongo import MongoClient
"""
pymongo
"""


def update_topics(mongo_collection, name, topics):
    """
    Args:
        mongo_collection: coleccion de la BD
        name: campo filtro para actualizar
        topics: campo que quiero actualizar

    Returns:
        el documento
    """
    #deberiamos buscar el documento por el nombre
    #deberiamos cambiar los topics de ese documento
    doc = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return doc