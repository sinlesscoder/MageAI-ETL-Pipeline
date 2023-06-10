import pandas as pd
from final_data_connection import engine

# Connection Object
con = engine.connect()

# Read the aliexpress_results table
df = pd.read_sql_table('aliexpress_results', con=con)

# View first 5 rows
print(df.head())