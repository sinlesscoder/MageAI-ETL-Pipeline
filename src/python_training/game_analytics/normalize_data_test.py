from normalizing_data import normalize_collection
import numpy as np
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI


cheapshark = 'cheapshark_col'
opencritic = 'opencritic_col'
db_name = 'Database_1'

# Sample object
result = normalize_collection(cheapshark, db_name)
result_1 = normalize_collection(opencritic, db_name)

print(result_1)

# Using keys() method
#column_names_keys = result.keys().tolist()
#print("Column names using keys() method:", column_names_keys)

# Using columns attribute
#column_names = result_1.columns.tolist()
#print("Column names using columns attribute:", column_names)

# mm = OpenAI(api_token="API_KEY")
# pandas_ai = PandasAI(mm, conversational=False)

# response = pandas_ai(result, "How many row has to do with batman?")
# print(response)