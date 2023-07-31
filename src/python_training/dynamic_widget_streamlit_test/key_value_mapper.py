from pandas import json_normalize
from mongo_db import connect_mongo
from pymongo.collection import Collection

mongo_uri = "mongodb://209.182.236.218:8975"
db = 'sample_db'

mongo_db = connect_mongo(mongo_uri, db)

# Show Collections
print(mongo_db.list_collection_names())

# Create a function called key_value mapper
def key_value_mapper(col: Collection):
    """
    Arguments:

    - col (MongoDB Collection from pymongo)

    Description:

    - Given the collection that you want to turn into a key,value mapper, retrieve first object and setup a
    logic that allows you to get the exact data types for each key.

    Output:

    - kv_mapper (dict) : Dictionary that has keys from MongoDB collection and values being data type.
    """

    # Get first document
    doc = next(col.find())

    # Create dictionary comprehension to get keys mapped to their value data types
    kv_mapper = {k : v for k, v in list(doc.items())[1:]}

    # Get the mapper as an output
    return kv_mapper

# Try with sample collection
sample = mongo_db['sample']

sample_kv = key_value_mapper(sample)

# If statement
def kvmapper(docs: list):

    # Convert docs into dataframe
    df = json_normalize(docs)

    # Dictionary to map keys to their types
    kv_mapped = {}

    # Get first row of dataframe
    first_row = df.iloc[0]

    for col in df.columns:
        if isinstance(first_row[col], int) or isinstance(first_row[col], float):
            # Add key,value pair for kv_mapped
            kv_mapped[col] = 'number'
        elif isinstance(first_row[col], str):
            kv_mapped[col] = 'string'
    
    return kv_mapped

sample_docs = [doc for doc in sample.find()]

print(kvmapper(sample_docs))
