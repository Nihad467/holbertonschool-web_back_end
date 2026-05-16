#!/usr/bin/env python3
"""Module that lists all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return all documents in a collection as a list."""
    return list(mongo_collection.find())
