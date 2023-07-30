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
def instance_control_flow(dictionary, val):
    if isinstance(dictionary[val], int):
        print("this is a numerical value")
    elif isinstance(dictionary[val], str):
        print("this is a string value")

instance_control_flow(sample_kv, 'name')

# print(isinstance('apple', str))

# ex = type('string')
# print(type(ex))