from sqlalchemy import create_engine
import pandas as pd

class StarbucksOrder:
    # Init Method: When someone runs the class, it initializes some steps
    def __init__(self, number_items: int):
        self.number_items = number_items

    # Order Method: 
    def order(self):
        i = 0
        # List of options for user input
        valid_options = ["drink", "breakfast", "lunch", "dinner", "pastry"]
        # List getting all the items
        results = []
        amount = self.number_items
        while i != amount:
            try:
                option = input(f"Enter an option:")
                if option not in valid_options:
                    raise ValueError("Invalid option.")
            except ValueError as e:
                print(e)
                continue

            results.append(option)
            i = i+1
        for r in results:
            print(r)
        return results

                
    # purchase_total Method: Adds up all of the item's price
    def purchase_total(self):
        j = 0
        lists = self.order()
        for item in lists:
            if item == "drink":
                j = j + 4
            if item == "lunch" or item == "dinner":
                j = j + 2
            if item == "pastry":
                j = j + 3
            if item == "breakfast":
                j = j + 3
        return j

# DuckDB Object Creation
def duckdb_connection(db_name: str):
    # Create the database dialect
    dialect = f'duckdb:///{db_name}'

    # Create connection to SQLAlchemy
    engine = create_engine(dialect)

    # Connection object
    con = engine.connect()

    print("DuckDB database connected successfully.")

    return con

# Function to load a DuckDB table
def load_duckdb_table(table_name: str):
    # Create duckdb connection
    cursor = duckdb_connection('starbucks.db')

    # Read the table_name as a pandas DataFrame
    result_df = pd.read_sql_table(table_name, con=cursor)

    return result_df

# Convert data list to pandas DataFrame
def create_df_from_objects(data_list):
    # Get the dictionary keys
    keys = list(data_list[0].keys())

    # Create an empty list
    result_list = {key : [] for key in keys}

    for obj in data_list:
        for key in keys:
            # Transform into dictionary with lists of similar keys in each
            result_list[key].append(obj[key])
    
    # Convert to pandas DataFrame
    return pd.DataFrame.from_dict(result_list)

# Function to turn DataFrame into SQL table in duckDB
def create_duckdb_sql_table(data):
    # Upload the data to pandas DataFrame
    result_df = create_df_from_objects(data)

    # Create duckdb connection
    duckdb_con = duckdb_connection('starbucks.db')

    # Export the DataFrame to a DuckDB table
    result_df.to_sql('results', con=duckdb_con, index=False, if_exists='replace')

    print("New records added to DuckDB database.")

starbuck = StarbucksOrder(5)
starbucks_df = create_df_from_objects(starbuck.order())

starbucks_sql = create_duckdb_sql_table(starbucks_df)

starbucks_df.to_sql('Orders', starbucks_sql)