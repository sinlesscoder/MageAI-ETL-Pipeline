import pandas as pd
from pymongo import MongoClient

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Retrieve Mongo Collection
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

# Common Data Model
def common_data_model(search_terms: list):
    """
    Inputs:
        - search_terms (list) : List of search terms retrieved by MongoDB
    Output:
        - final_df (pd DataFrame): DataFrame that contains consolidated results of terms and page numbers.
    """
    # List to store DataFrames of each term with specific page
    frames = []

    for term in search_terms:
        # Retrieve data from MongoDB Collection
        term_col = retrieve_mongo_connection(term)

        # Use .find() on the collection
        docs = list(term_col.find())

        # Getting specific object from collection
        doc = docs[0]

        # Specifying page numbers 1 through 2
        page_numbers = [str(i) for i in range(1, 3)]

        # Run in a loop
        for num in page_numbers:
            # Control flow to see if the object actually has results
            ## If it does, normalize it to get a DataFrame
            if 'result' in doc[num].keys():
                results = doc[num]['result']['resultList']
                df = pd.json_normalize(results)
                
                # Updating the DataFrame with columns of page number and search term
                df['page_number'] = num
                df['search_term'] = term
                frames.append(df)
            else:
                # Quick logging to mention that a certain object doesn't have results
                print("Your quota exceeded. Cannot make dataframe.")

    # Concatenate the final DataFrame
    final_df = pd.concat(frames)

    return final_df


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    cdm_df = common_data_model(data)

    return cdm_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
