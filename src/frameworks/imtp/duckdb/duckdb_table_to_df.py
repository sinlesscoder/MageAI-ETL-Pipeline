import duckdb

# Setup a connection
connection = duckdb.connect('example.db')

# duckdb.sql
query = 'SELECT col1 FROM csv_example'

result = duckdb.sql(query=query, connection=connection)

print(result)

# Convert to a DataFrame
df = result.df()

print(df)

# Finding all tables within the duckDB database
tables_query = 'SELECT DISTINCT table_name FROM INFORMATION_SCHEMA.columns'

all_tables = duckdb.sql(tables_query, connection=connection)

print(all_tables)