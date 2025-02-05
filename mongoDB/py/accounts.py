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

with open("accounts.json", "r") as file:
    data = json.load(file)

result = collection.insert_many(data)

print("Inserted data with the following IDs:", result.inserted_ids)

index_name = "city_index"
collection.create_index("address.city", name=index_name)

city = "Bradshawborough"
results = collection.find({"address.city": city})

for result in results:
    print(result)

min_balance = 30000
results = collection.find({"balance": {"$gt": min_balance}})

for result in results:
    print(result)