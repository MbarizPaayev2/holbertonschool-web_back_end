#!/usr/bin/env python3
import pymongo 
def list_all(mongo_collection):
    return list(db.school.find())

