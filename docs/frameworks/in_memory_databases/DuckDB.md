## DuckDB Fundamentals

### Description

- In Memory Transaction Processing: Whenever someone creates a SQL table or is performing a query, we are performing a `transaction`.

- Transactions generally happen within a database:

  - Schemas
  - Tables
  - Creating new databases
  - Deleting databases

- Transactions with other files in the same directory.

  - Interacts with a `.csv` file
  - Interacts with a `.parquet` file

- Auto-generate databases and store tables within them using a connection object.

### Installation

- Via `pip`

```bash
pip install duckdb
```

### Example Usage

- With `python`
- Save data from a CSV file into a duckdb table.

```python
import duckdb

# Setup a connection
connection = duckdb.connect('example.db')

# Turn the connection into a cursor object
cursor = connection.cursor()

# CSV File: example.csv
file_name = 'example.csv'

# Save CSV results into table
cursor.execute(f'CREATE TABLE example AS (SELECT * FROM load_auto_csv({file_name}))')

# Close the cursor
cursor.close()
```

- Convert a duckdb SQL query into a pandas DataFrame

```python
import duckdb

# Setup your connection
connection = duckdb.connect('example.db')

# duckdb.sql
result = duckdb.sql('SELECT * FROM example', connection=connection)

# Convert the result into a pandas DataFrame
df = result.df()

print(df)
```

### Resources

- [duckDB Documentation](https://duckdb.org/docs/archive/0.2.9/)
