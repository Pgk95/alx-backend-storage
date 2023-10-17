#!/usr/bin/env python3
"""Mongo db script"""

from pymongo import MongoClient
# Conncect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the "logs" database and "nginx" collection
db = client["logs"]
collection = db["nginx"]

# count the totla number of documents in the collection
total_logs = collection.count_documents({})

# counts the total number of documents
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {}

for method in methods:
    method_counts[method] = collection.count_documents({"method": method})

# count the number of documents with method=GET and path=/status
status_path_count = collection.count_documents({"method": "GET",
                                                "path": "/status"})

# print the results
print(f"{total_logs} logs where {total_logs} is the number of documents in the collection")
print("Methods:")
for method in methods:
    print(f"{status_path_count} logs with method=GET and path=/status")
