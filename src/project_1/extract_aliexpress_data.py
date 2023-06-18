import requests

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

    headers = {
        "X-RapidAPI-Key": "90d6f20e25msh26f3b3c0cc23025p1fa1dajsn46ee4c3bd0d5",
        "X-RapidAPI-Host": "aliexpress-datahub.p.rapidapi.com"
    }

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