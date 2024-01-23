#!/usr/bin/env python3
"""
python function to list all documents in a collection
"""


def list_all(mongo_collection):
    """ function to list all documents"""
    return mongo_collection.find()
