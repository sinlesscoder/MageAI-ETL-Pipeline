import ast
import pandas as pd
from load_mongodb import retrieve_mongo_connection

# Retrieve data from MongoDB Collection
iphone_col = retrieve_mongo_connection('iphone')

# Use .find() on the collection
docs = list(iphone_col.find())

doc = docs[0]

#print(doc)

#print("---------------------------------------")

# Keys of the document
#print(doc.keys())

#print("---------------------------------------")

#print(doc['updated_at'])

#print("---------------------------------------")

# Page 1 Results
page_1_results = doc['1']['result']
#print(type(page_1_results))

#print("---------------------------------------")

# Look at page 1's keys
#print(page_1_results.keys())

#print("---------------------------------------")

# What's in status?
status_df = pd.DataFrame(page_1_results['status'], index=[0])
#print(status_df)

#print("---------------------------------------")

# What's in setting?
settings_df = pd.DataFrame(page_1_results['settings'], index=[0])
#print(settings_df)

#print("---------------------------------------")

# What's in base?
#print(page_1_results['base'].keys())

#print("---------------------------------------")

# Result List
r_list = page_1_results['resultList']
#print(type(r_list))
#print(len(r_list))
#print(type(r_list[1]))
print(r_list[1].keys())

print("---------------------------------------")

result_df = pd.DataFrame()

x = 0

for i in range(len(r_list)):
    # Item vs Delivery
    sample_result = r_list[i]

    ## Item Key
    sample_result_df = pd.DataFrame(sample_result['item'], index=[0])

    sample_result_df['sku'].fillna(str(sample_result['item']['sku']), inplace=True)

    #print(sample_result_df.columns)

    #print("---------------------------------------")

    #print(sample_result_df[['sku', 'title', 'image']].head())

    #print("---------------------------------------")

    #print(sample_result_df['sku'].dtype)

    #print("---------------------------------------")

    # Test to see if the column will be a dictionary or null
    sample_result_df['sku'] = sample_result_df['sku'].apply(lambda x: ast.literal_eval(x))

    #print(sample_result_df['sku'].iloc[0]['def']['prices'])

    #print("---------------------------------------")

    # JSON Normalize
    sku_df = pd.json_normalize(sample_result_df['sku'])

    sku_df['price_comparison'] = sku_df['def.prices.pc'].equals(sku_df['def.prices.app'])

    # Counting the number of FALSE
    if not sku_df['price_comparison'].all():
        x = x + 1
    # Append sku_df to result_df
    result_df = pd.concat([result_df, sku_df], ignore_index=True)

print(result_df)
print('-------------------------')
print(x)