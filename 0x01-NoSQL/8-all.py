#!/usr/bin/env python3
"""
list collections using pymongo
"""


def list_all(mongo_collection):
    """
    list all documents in a collection
    """
    documents = mongo_collection.find({})
    if documents.count() == 0:
        return []
    return documents
