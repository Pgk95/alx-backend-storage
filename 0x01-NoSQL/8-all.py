#!/usr/bin/env python3
"""mongodb script"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    document_list = []
    cursor = mongo_collection.find()

    for document in cursor:
        document_list.append(document)
    return document_list
    