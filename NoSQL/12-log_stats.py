#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient
"""
pymongo
"""

def log_stats():
    """proporciona estadisticas"""

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})
    print("{} logs".format(total_logs))


    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_checks = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_checks))

if __name__ == "__main__":
    log_stats()
