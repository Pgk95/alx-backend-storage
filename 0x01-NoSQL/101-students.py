#!/usr/bin/env python3
"""mongodb script"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    students = mongo_collection.find().sort("averageScore", -1)

    sorted_students = list(students)

    for student in sorted_students:
        student["averageScore"] = round(student["averageScore"], 2)
    
    return sorted_students
