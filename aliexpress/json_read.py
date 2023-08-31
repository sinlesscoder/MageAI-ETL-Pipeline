from json import load
from os import getcwd

def json_reader(key: str):
    """
    Input: 
        - Name of the private key

    Output:
        - Data from the private key
        
    """
    # Load JSON data from the file
    keys_path = getcwd() + "/aliexpress"

    with open(f"{keys_path}/hidden.json", "r") as f:
        config_data = load(f)

    # Access the URI
    uri = config_data[key]

    return uri