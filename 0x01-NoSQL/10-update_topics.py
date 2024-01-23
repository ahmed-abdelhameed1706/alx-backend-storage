#!/usr/bin/env python3
"""function to change school topics"""


def update_topics(mongo_collection, name, topics):
    """function to update topics"""
    mongo_collection.update_many({"name": name},{"$set":{"topics": topics}})
