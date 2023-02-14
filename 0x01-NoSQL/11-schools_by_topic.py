#!/usr/bin/env python3
"""
find a specific item in a collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    return mongo_collection.find({"topics": topic})
