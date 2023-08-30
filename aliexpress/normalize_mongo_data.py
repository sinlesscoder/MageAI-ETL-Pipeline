import pandas as pd
from load_mongodb import retrieve_mongo_connection

# Search result term
search_terms = ['samsung_galaxy_s22', 'iphone']


def common_data_model(search_terms: list):
    frames = []

    for term in search_terms:
        # Retrieve data from MongoDB Collection
        term_col = retrieve_mongo_connection(term)

        # Use .find() on the collection
        docs = list(term_col.find())

        doc = docs[0]

        page_numbers = [str(i) for i in range(1, 3)]

        # Run in a loop
        for num in page_numbers:
            if 'result' in doc[num].keys():
                results = doc[num]['result']['resultList']
                df = pd.json_normalize(results)
                df['page_number'] = num
                df['search_term'] = term
                frames.append(df)
            else:
                print("Your quota exceeded. Cannot make dataframe.")

    # Concatenate the final DataFrame
    final_df = pd.concat(frames)

    return final_df

result = common_data_model(search_terms)

print(result.keys())