#!/usr/bin/env python3
"""function to get students by average score"""
import pymongo


def top_students(mongo_collection):
    """function to find the sort the students"""
    students = mongo_collection.find()

    for student in students:
        topics = student["topics"]
        sum_score = sum(topic["score"] for topic in topics)

        averageScore = sum_score / len(topics)

        mongo_collection.update_one(
            {"_id": student["_id"]},
            {"$set": {"averageScore": averageScore}}
        )

    sorted_students = mongo_collection.find().sort("averageScore", pymongo.DESCENDING)

    return sorted_students
