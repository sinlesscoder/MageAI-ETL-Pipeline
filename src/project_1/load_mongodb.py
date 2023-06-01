from extract_aliexpress_data import retrieve_item_pages
from pymongo import MongoClient
from datetime import datetime

# Connection to MongoDB

def retrieve_mongo_connection(search_term: str, uri='104.225.217.176:8363'):
    """
    Inputs:
        - search_term (string): Search term for the query of API
        - uri (string): Uniform Resource Identifier to represent MongoDB server
    
    Output:
        - collection_name (Mongo.Collection): Collection to store your results.
    """
    # Set up a Mongo Client
    client = MongoClient(uri)

    # Select a database
    database = client['aliexpress_items']

    # Select a collection
    collection_name = database[search_term]

    return collection_name

# Prepare Data
def prepare_data_mongo(search_term: str):
    """
    Inputs:
        - search_term (string): Search query for item information
    Output:
        - result_dict (dictionary): Dictionary containing key, 
            values of page number mapped to actual JSON result
    """
    # Get results
    results = retrieve_item_pages(search_term)

    # Convert above into a dictionary
    result_dict = {f"{i+1}" : result for i, result in enumerate(results)}

    return result_dict

def db_load(search_term: str):
    """
    Inputs:
        - search_term (string)
    Output:
        - result_dict (dictionary): Dictionary containing results
            with pages as keys
    """
    # Get the Mongo collection
    collection_name = retrieve_mongo_connection(search_term)

    # Get the result dictionary
    result_dict = prepare_data_mongo(search_term)

    # Getting current date time as a string
    result_dict['updated_at'] = str(datetime.now())

    # Insert the Dictionary as an Object in the MongoDB Collection
    collection_name.insert_one(result_dict)

    return result_dict


