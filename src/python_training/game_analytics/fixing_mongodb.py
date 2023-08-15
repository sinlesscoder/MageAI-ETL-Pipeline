from pymongo import MongoClient

# Delete the database
def drop_collection(database: str, col: str, uri='209.182.236.218:8057'):
    # Set up a Mongo Client
    client = MongoClient(uri)
    db = client[database]
    db.drop_collection(col)

    client.close()

# Rename collection name
def rename_col(old_name: str, new_name: str, database: str, uri='209.182.236.218:8057'):
    # Set up a Mongo Client
    client = MongoClient(uri)
    db = client(database)
    db[old_name].rename(new_name)

# List database names
def database_names(uri='209.182.236.218:8057'):
    client = MongoClient(uri)
    db_names = client.list_database_names()

    for name in db_names:
        print(name)

    client.close()

# List collection names
def list_names(database: str, uri='209.182.236.218:8057'):
    client = MongoClient(uri)
    db = client[database]
    collection_names = db.list_collection_names()

    for name in collection_names:
        print(name)

    client.close()