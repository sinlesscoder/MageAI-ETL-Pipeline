from rapidapi import retrieve_item_pages
from pymongo import MongoClient
from datetime import datetime

# Connection to MongoDB

def retrieve_mongo_connection(collection_name: str, database_name: str, uri='209.182.236.218:8057'):
    """
    Inputs:
        - search_term (string): Search term for the query of API
        - uri (string): Uniform Resource Identifier to represent MongoDB server
    
    Output:
        - collection_name (Mongo.Collection): Collection to store your results.
    """
    # Set up a Mongo Client
    client = MongoClient(uri)

    # Create a database
    database = client[database_name]

    # Create a collection
    collection = database[collection_name]

    return collection

def retrieve_all_collections(database_name: str, uri='209.182.236.218:8057') -> dict:
    # Set up a Mongo Client
    client = MongoClient(uri)

    # Create a database
    database = client[database_name]

    # See all the collections
    results = database.list_collection_names()

    # Dictionary for All Collections
    col_dict = {col: [obj for obj in col.find()] for col in results}

    return col_dict




# # Prepare Data
# def prepare_data_mongo(search_term: str):
#     """
#     Inputs:
#         - search_term (string): Search query for item information
#     Output:
#         - result_dict (dictionary): Dictionary containing key, 
#             values of page number mapped to actual JSON result
#     """
#     # Get results
#     results = retrieve_item_pages(search_term)

#     # Convert above into a dictionary
#     result_dict = {f"{i+1}" : result for i, result in enumerate(results)}

#     return result_dict

# def db_load(search_term: str):
#     """
#     Inputs:
#         - search_term (string)
#     Output:
#         - result_dict (dictionary): Dictionary containing results
#             with pages as keys
#     """
#     # Get the Mongo collection
#     collection_name = retrieve_mongo_connection(search_term)

#     # Get the result dictionary
#     result_dict = prepare_data_mongo(search_term)

#     # Getting current date time as a string
#     result_dict['updated_at'] = str(datetime.now())

#     # Insert the Dictionary as an Object in the MongoDB Collection
#     collection_name.insert_one(result_dict)

#     return result_dict