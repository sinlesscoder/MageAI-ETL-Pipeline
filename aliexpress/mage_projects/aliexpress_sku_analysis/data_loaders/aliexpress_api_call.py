import requests
from pymongo import MongoClient
from json_read import json_reader

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def search_item(search_query: str, page_number: int):
    """
    Inputs:
        - search_query: string
        - page_number: integer
    
    Output:
        - result: dict or list (depending on the JSON output)    
    
    """
    url = "https://aliexpress-datahub.p.rapidapi.com/item_search"

    querystring = {"q":search_query,"page":page_number}

    key = json_reader("X-RapidAPI-Key")
    host = json_reader("X-RapidAPI-Host")

    headers = {key, host}

    response = requests.get(url, headers=headers, params=querystring)

    result = response.json()

    return result

def retrieve_item_pages(search_query: str):
    """
    Inputs:
        - search_query (string): Query that a user submits to get item information
    
    Output:
        - page_results (list): List of results from API for first 2 pages
    """
    # Page Results
    page_results = []
    
    # Iterate over the first 2 pages
    for i in range(1, 3):
        result = search_item(search_query, i)
        page_results.append(result)
    
    return page_results

# Helper Function for viewing currently existing collections
def retrieve_collection_names(db_name: str):
    
    uri = json_reader("URI")

    client = MongoClient(uri)

    db = client[db_name]

    # See all the collections
    results = db.list_collection_names()

    print(results)

    return results

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here

    ## Use the above helper function

    current_collections = retrieve_collection_names('aliexpress_items')

    all_terms = ['laptop', 'phone', 'ipad', 'iphone', 'samsung galaxy s22']

    search_terms = [term for term in all_terms if term not in current_collections]

    dictionary = {}

    for term in search_terms:
        dictionary[term] = retrieve_item_pages(term)

    return dictionary


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
