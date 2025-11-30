#!/usr/bin/env python3
"""this is comment"""


def schools_by_topic(mongo_collection, topic):
    """this is comment"""
    return list(mongo_collection.find({"topic": topic }))
