from normalizing_data import normalize_collection
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Sample object
cheapshark_df = normalize_collection('cheapshark_col', 'Database_1')
opencritic_df = normalize_collection('opencritic_col', 'Database_1')

def mismatch(col_name: str, col_name_2: str, database: str):
    df = normalize_collection(col_name, database)
    df_2 = normalize_collection(col_name_2, database)
    for i in range(len(df_2)):
        for j in range(len(df)):
            result = fuzz.partial_ratio(df_2.loc[i,'name'],df.loc[j, 'title'])
            if result >= 80:
                print(str(result) + ' - ' + df_2.loc[i,'name'] + ' -- ' + df.loc[j, 'title'])

mismatch('cheapshark_col', 'opencritic_col', 'Database_1')