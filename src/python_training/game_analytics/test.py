from load_mongodb import db_load
import pandas as pd
from load_mongodb import retrieve_mongo_connection
from rapidapi import search_item, retrieve_item_pages, retrieve_item_2_pages
import json
import pymongo


# Select a search term
search_terms = 'batman'

# rapid_one = search_item(search_terms,1)

# retrieve_mongo_connection(search_terms, )

# def common_data_model(search_terms: list):
#     frames = []

#     for term in search_terms:
#         # Retrieve data from MongoDB Collection
#         term_col = retrieve_mongo_connection(term)

#         # Use .find() on the collection
#         docs = list(term_col.find())

#         doc = docs[1]

#         page_numbers = [str(i) for i in range(1, 2)]

#         # Run in a loop
#         for num in page_numbers:
#             if 'result' in doc[num].keys():
#                 results = doc[num]['result']['resultList']
#                 df = pd.json_normalize(results)
#                 df['page_number'] = num
#                 df['search_term'] = term
#                 frames.append(df)
#             else:
#                 print("Your quota exceeded. Cannot make dataframe.")

#     # Concatenate the final DataFrame
#     final_df = pd.concat(frames)

#     return final_df

# result = common_data_model(search_terms)

# print(result.tail())


data1 = retrieve_item_2_pages(search_terms)
data2 = retrieve_item_pages(search_terms)

# Data from search 1
df1 = pd.DataFrame(data1)

# Data from search 2
#df2 = pd.DataFrame(data2)

col = retrieve_mongo_connection
col.insert_one(df1)
# Merge DataFrames using 'batman' as the key
#merged_df = pd.merge(df1, df2, on='internalName', how='inner') 

#column_names = df2.columns.tolist()

#print(column_names)
