import duckdb

# Connection
connection = duckdb.connect('example.db')

# Turn the connection into a cursor object
cursor = connection.cursor()

# Reference a CSV file
file_name = 'example.csv'

# Save the CSV Results into a new table called csv_example
query = f'CREATE TABLE csv_example AS ( \
SELECT * \
FROM read_csv_auto({file_name}) \
)'

# Execute this query to create the table
cursor.execute(query)

# Close the cursor
cursor.close()