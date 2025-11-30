#!/usr/bin/env python3
"""this is docstr"""


def update_topics(mongo_collection, name, topics):
    """this is docstr"""
    mongo_collection.update_many(
        {"name":name},
        {"$set" { "topics":}}
    )