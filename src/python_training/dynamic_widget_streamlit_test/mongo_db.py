from pymongo import MongoClient

def connect_mongo(uri: str, database: str):
    # Setup the MongoClient
    client = MongoClient(uri)

    # Database
    db = client[database]

    return db

