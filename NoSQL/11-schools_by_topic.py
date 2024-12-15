#!/usr/bin/env python3
"""
python
"""
from pymongo import MongoClient
"""
pymongo
"""


def schools_by_topic(mongo_collection, topic):
    """

    Args:
        mongo_collection: coleccion donde buscar
        topic: topic para filtrar

    Returns:
        documentos filtrados
    """
    return mongo_collection.find({"topics": topic})