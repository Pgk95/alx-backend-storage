#!/usr/bin/env python3
"""mongodb scripts"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document into a collection"""
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id