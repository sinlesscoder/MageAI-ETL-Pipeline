import numpy as np
import pandas as pd
from setup_duckdb_connection import setup_duckdb_engine, setup_duckdb_db
from os import getcwd

# DB Path
db_path = getcwd() + "/src/python_training/duckdb_connection"

setup_duckdb_db('example.db')

# Create some random data
df = pd.DataFrame(np.random.randint(0, 1000, size=(10000, 5)))

# Rename the columns
df.columns = [f'col{i+1}' for i in range(5)]

# DuckDB Connection
duckdb_cursor = setup_duckdb_engine('example.db')

duckdb_con = duckdb_cursor.connect()

# Pandas to_sql
## Contains both transformation and the loading from DataFrame to DuckDB SQL.
df.to_sql('sample', con=duckdb_con, index=False, if_exists='replace')

print("DataFrame converted to DuckDB table :)")