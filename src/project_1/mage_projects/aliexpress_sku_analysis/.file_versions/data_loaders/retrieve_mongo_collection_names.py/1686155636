from pymongo import MongoClient

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Helper Function
def retrieve_collection_names(db_name: str):
    uri='104.225.217.176:8363'

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
    search_terms = retrieve_collection_names('aliexpress_items')

    return search_terms


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
