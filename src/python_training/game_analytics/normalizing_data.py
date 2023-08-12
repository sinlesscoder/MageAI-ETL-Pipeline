import pandas as pd
from load_mongodb import retrieve_mongo_connection

# Helper Function: Normalize Collection
def normalize_collection(col_name: str, db_name: str):
    # Retrieving the collection from Mongo Client
    col = retrieve_mongo_connection(col_name, db_name)

    # Retrieve all documents in the collection
    docs = [obj for obj in col.find()]

    # Transform the JSON into a DataFrame
    df = pd.json_normalize(docs)

    return df




# def common_data_model(search_terms: list):
#     frames = []

#     for term in search_terms:
#         # Retrieve data from MongoDB Collection
#         term_col = retrieve_mongo_connection('collection_2', 'Database_1')

#         # Use .find() on the collection
#         docs = list(term_col.find())

#         doc = docs[0]

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
