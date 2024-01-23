#!/usr/bin/env python3
"""function to insert documents"""


def insert_school(mongo_collection, **kwargs):
    """function to insert documents"""
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
