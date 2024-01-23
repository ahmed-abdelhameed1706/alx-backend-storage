#!/usr/bin/env python3
""" script to get some stats from logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    """script to get some stats from logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{db.count_documents({})} logs")

    print("Methods:")

    for method in methods:
        print(f"\tmethod {method}: {db.count_documents({'method': method})}")

    query = {'method': 'GET', 'path': '/status'}

    print(f"{db.count_documents(query)} status check")

    print("IPS:")

    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
            {"$project": {"_id": 0, "ip": "$_id", "count": 1}}
            ]

    ips = db.aggregate(pipeline)

    for ip in ips:
        print(f"\t{ip['ip']}: {ip['count']}")
