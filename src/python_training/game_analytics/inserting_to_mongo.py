from load_mongodb import db_load
import pandas as pd
from load_mongodb import retrieve_mongo_connection
from rapidapi import search_item, search_item_2, retrieve_item_pages, retrieve_item_2_pages

# Select a search term
search_terms = 'batman'

#data1 = search_item(search_terms,1)
data2 = search_item_2(search_terms,1)

#col = retrieve_mongo_connection('collection_1', 'Database_1')
col2 = retrieve_mongo_connection('collection_2', 'Database_1')

#col.insert_one(data1)
col2.insert_many(data2)
print("Insertion successful")
print(col2.find())
