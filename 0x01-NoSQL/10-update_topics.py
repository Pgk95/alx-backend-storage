#!/usr/bin/env python3
"""mongo db script"""


def update_topics(mongo_collections, name, topics):
    """Changes all topics of a school document based on the name"""
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}
    result = mongo_collections.update_many(filter_query, update_query)
    return result.modified_count