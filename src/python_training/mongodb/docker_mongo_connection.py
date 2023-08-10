import json
from pymongo import MongoClient
from os import getcwd

# Data Path to the Password for MongoDB Atlas
creds_path = getcwd() + "/src/python_training/mongodb"

# Setup a local variable called MONGODB_ATLAS_PASSWORD
with open(f"{creds_path}/mongodb_atlas_connection.json", "r") as f:
    mongo_atlas_creds = json.load(f)

# Use locals().update() to get a new variable in the script called MONGODB_ATLAS_PASSWORD
locals().update(mongo_atlas_creds)

# Add your Uniform Resource Identifier from MongoDB Atlas

uri = MONGODB_DOCKER_CONNECTION

# Setup a MongoClient
client = MongoClient(uri)

# Create a database
db = client['sample']

# Sample dictionary
sample_dict = {'ex1': 1}

# Create a collection
col = db['sample_collection']

# Update the collection with the sample dictionary
col.insert_one(sample_dict)

print("Collection saved successfully :)")