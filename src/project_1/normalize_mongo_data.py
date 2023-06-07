import pandas as pd
from load_mongodb import retrieve_mongo_connection

# Retrieve data from MongoDB Collection
iphone_col = retrieve_mongo_connection('iphone')

# Use .find() on the collection
docs = list(iphone_col.find())

doc = docs[0]

page_numbers = [str(i) for i in range(1, 3)]

print(page_numbers)

# First Page
page_one = doc[page_numbers[0]]

page_one_results = page_one['result']['resultList']

page_one_df = pd.json_normalize(page_one_results)

print(page_one_df.info())