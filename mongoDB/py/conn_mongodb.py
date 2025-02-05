# Connecting to MongoDB
from pymongo import MongoClient
import pymongo
import json

client = MongoClient('mongodb://localhost:27017/')
# Creating a database
db = client['mongoTp']
# Creating a collection      
collection = db['tp-collection']
print(collection.collection)

# Inserting a document
document = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

# Inserting multiple documents
documents = [
    {"name": "Alice", "email": "alice@example.com", "age": 25},
    {"name": "Bob", "email": "bob@example.com", "age": 35}
]
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)

# Querying for a document
query = {"name": "John Doe"}
document = collection.find_one(query)
print(document)

# Multiple querying for documents
query = {"age": {"$gt": 25}}
documents = collection.find(query)
for doc in documents:
    print(doc)

# Updating a document
query = {"name": "John Doe"}
update = {"$set": {"age": 31}}
result = collection.update_one(query, update)
print("Modified document count:", result.modified_count)

# Updating multiple documents
query = {"age": {"$gt": 25}}
update = {"$inc": {"age": 1}}
result = collection.update_many(query, update)
print("Modified document count:", result.modified_count)

# Deleting a document
query = {"name": "John Doe"}
result = collection.delete_one(query)
print("Deleted document count:", result.deleted_count)

# Multiple deleting documents
query = {"age": {"$gt": 25}}
result = collection.delete_many(query)
print("Deleted document count:", result.deleted_count)

# Querying and Filtering Data
query = {
    "$and": [
        {"age": {"$gt": 25}},
        {"email": {"$regex": "@example\.com$"}}
    ]
}
documents = collection.find(query)

for doc in documents:
    print(doc)

# Projection in MongoDB
query = {"age": {"$gt": 25}}
projection = {"_id": 0, "name": 1, "email": 1}
documents = collection.find(query, projection)

for doc in documents:
    print(doc)
    
# Sorting in MongoDB
query = {"age": {"$gt": 25}}
documents = collection.find(query).sort("name", pymongo.ASCENDING)

for doc in documents:
    print(doc)
    
