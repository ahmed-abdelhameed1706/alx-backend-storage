#!/usr/bin/env python3
"""function to select schools based on topics"""


def schools_by_topic(mongo_collection, topic):
    """function to return list of schools based on topic"""
    return mongo_collection.find({"topics": {"$in": [topic]}})
