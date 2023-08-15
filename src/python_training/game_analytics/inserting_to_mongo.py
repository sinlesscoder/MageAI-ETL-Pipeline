from load_mongodb import retrieve_mongo_connection
from rapidapi import opencritic_game_search, cheapshark_game_deals

# Select a search term
search_terms = 'batman'

data1 = opencritic_game_search(search_terms)
data2 = cheapshark_game_deals(search_terms,1)

col = retrieve_mongo_connection('opencritic_col', 'Database_1')
col2 = retrieve_mongo_connection('cheapshark_col', 'Database_1')

#col.insert_one(data1)
col2.insert_many(data2)
print("Insertion successful")
print(col2.find())