#!/usr/bin/env python3
"""this is docstring"""
import pymongo

client = MongoClient('mongodb://127.0.0.1:27017')  
dbs = logs
collection = nginx 
total_logs = collection.count_documents({})
print("{}".format(total_logs))

for i in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    collection.count_documents({"method": i})
    print("{}:{}".format(Method, i))
status_check = collection.count_documents({"method": "GET", "path": "/status"})
print("{}".format(status_check))