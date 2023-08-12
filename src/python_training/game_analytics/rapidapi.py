import requests

def opencritic_game_search(game_name: str):
    """
    Inputs:
        - search_query: string
        - page_number: integer
    
    Description:
        - This function is meant to perform a request to the OpenCritic API to get details about a video game.
    
    Output:
        - result: dict or list (depending on the JSON output)    
    
    """
    import requests

    url = "https://opencritic-api.p.rapidapi.com/game/search"

    querystring = {"criteria": game_name}

    headers = {
        "X-RapidAPI-Key": "90d6f20e25msh26f3b3c0cc23025p1fa1dajsn46ee4c3bd0d5",
        "X-RapidAPI-Host": "opencritic-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    result = response.json()

    return result

def cheapshark_game_deals(search_query: str, page_number: int):
    """
    Inputs:
        - search_query: string
        - page_number: integer
    
    Output:
        - result: dict or list (depending on the JSON output)    
    
    """
    url = "https://cheapshark-game-deals.p.rapidapi.com/deals"

    page_index = page_number - 1

    querystring = {"lowerPrice":"0","steamRating":"0","title":search_query,"desc":"0","output":"json","steamworks":"0","sortBy":"Deal Rating","pageSize":"60","exact":"0","pageNumber":page_index,"onSale":"0","metacritic":"0","storeID[0]":"1,2,3"}

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
    for i in range(1, 4):
        result = cheapshark_game_deals(search_query, i)
        page_results.append(result)
    
    return page_results