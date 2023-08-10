import pytest
import duckdb
import pandas as pd
from setup_duckdb_connection import setup_duckdb_engine

# Connect to the database directly with duckdb
db = duckdb.connect('example.db')

# Engine connection for duckdb-engine
duckdb_engine = setup_duckdb_engine('example.db')

duckdb_con = duckdb_engine.connect()

# Get the table as a pandas DataFrame
df = duckdb.sql("SELECT * FROM sample", connection=db).df()

# Unit Test #1: Does the DataFrame from the table have 10,000 rows
def test_df_rows():
    
    assert df.shape[0] == 10000


# Unit Test #2 : Does the DataFrame from the table have 5 columns
def test_df_cols():

    assert df.shape[1] == 5


# Unit Test #3 : Does the duckdb-connection directly allow the DataFrame to read the data?
def test_df_from_connection():
    con_df = pd.read_sql_table('sample', con=duckdb_con)

    assert isinstance(con_df, pd.DataFrame)