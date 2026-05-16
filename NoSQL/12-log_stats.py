#!/usr/bin/env python3
"""Script that provides statistics about Nginx logs."""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs_collection = client.logs.nginx

    logs_count = logs_collection.count_documents({})
    print("{} logs".format(logs_count))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        method_count = logs_collection.count_documents(
            {"method": {"$eq": method}}
        )
        print("\tmethod {}: {}".format(method, method_count))

    status_count = logs_collection.count_documents(
        {
            "$and": [
                {"method": {"$eq": "GET"}},
                {"path": "/status"}
            ]
        }
    )
    print("{} status check".format(status_count))
