import requests

def search_item(search_query: str, page_number: int):
    """
    Inputs:
        - search_query: string
        - page_number: integer
    
    Output:
        - result: dict or list (depending on the JSON output)    
    
    """
    url = "https://opencritic-api.p.rapidapi.com/game/search"

    querystring = {"criteria":"the withcer 3"}

    headers = {
        "X-RapidAPI-Key": "ec2578b31bmsh1c07c7237ff7875p181132jsnd6768d4a7029",
        "X-RapidAPI-Host": "opencritic-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    result = response.json()

    return result

def search_item_2(search_query: str, page_number: int):
    """
    Inputs:
        - search_query: string
        - page_number: integer
    
    Output:
        - result: dict or list (depending on the JSON output)    
    
    """
    url = "https://cheapshark-game-deals.p.rapidapi.com/deals"

    querystring = {"lowerPrice":"0","steamRating":"0","title":"batman","desc":"0","output":"json","steamworks":"0","sortBy":"Deal Rating","AAA":"0","pageSize":"60","exact":"0","upperPrice":"50","pageNumber":"0","onSale":"0","metacritic":"0","storeID[0]":"1,2,3"}

    headers = {
        "X-RapidAPI-Key": "ec2578b31bmsh1c07c7237ff7875p181132jsnd6768d4a7029",
        "X-RapidAPI-Host": "cheapshark-game-deals.p.rapidapi.com"
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
    
    # Iterate over the first 1 pages
    for i in range(1, 2):
        result = search_item(search_query, i)
        page_results.append(result)
    
    return page_results