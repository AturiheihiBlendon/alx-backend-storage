#!/usr/bin/env python3
"""
Insert a document in Python
"""

def insert_school(mongo_collection, **kwargs):
    """returns id of the inserted document
    """
    return mongo_collection.insert(kwargs)
