#!/usr/bin/env python3
""" script to get some stats from logs"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs.nginx

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print(f"{db.count_documents({})} logs")

print("Methods:")

for method in methods:
    print(f"\tmethod {method}: {db.count_documents({'method': method})}")

print(f"{db.count_documents({'method':'GET', 'path':'/status'})} status check")
