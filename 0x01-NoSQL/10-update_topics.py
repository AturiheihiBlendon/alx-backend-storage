#!/usr/bin/env python3
"""
Update school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    q = {"name": name}
    values = {"$set": {"topics": topics}}

    mongo_collection.update_many(q, values)
