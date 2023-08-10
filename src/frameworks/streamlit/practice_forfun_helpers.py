import pandas as pd
from streamlit import image
from sqlalchemy import create_engine
from skimage.io import imread


# Create the data object as a function
def create_object(username, password, bio, image_url):
    infos = {
        'username' : username,
        'password': password,
        'bio': bio,
        'image': image_url
    }

    return infos

# Convert data list to pandas DataFrame
def create_df_from_objects(data_list):
    # Get the dictionary keys
    keys = list(data_list[0].keys())

    # Create an empty dictionary
    infos_dict = {key : [] for key in keys}

    for obj in data_list:
        for key in keys:
            # Transform into dictionary with lists of similar keys in each
            infos_dict[key].append(obj[key])
    
    # Convert to pandas DataFrame
    return pd.DataFrame.from_dict(infos_dict)

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
    cursor = duckdb_connection('infos.db')

    # Read the table_name as a pandas DataFrame
    infos_df = pd.read_sql_table(table_name, con=cursor)

    return infos_df

# Create a function that turns a DataFrame into a data_list
def df_to_data_list(df: pd.DataFrame):
    # Create the data list
    data_list = []

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Go through each row
    for i in range(df.shape[0]):
        # Get the row
        row = df.iloc[i]

        # Create the object from the row
        obj = create_object(row['username'], row['password'], row['bio'], row['image'])

        # Add the object to the data list
        data_list.append(obj)
    
    return data_list

# Function to turn DataFrame into SQL table in duckDB
def create_duckdb_sql_table(data):
    # Upload the data to pandas DataFrame
    infos_df = create_df_from_objects(data)

    # Create duckdb connection
    duckdb_con = duckdb_connection('infos.db')

    # Export the DataFrame to a DuckDB table
    infos_df.to_sql('infos', con=duckdb_con, index=False, if_exists='append')

    print("New records added to DuckDB database.")

# Create a function to create a numpy array from the image_url
def create_array_from_url(image_url: str):
    # Numpy array of the image URL's content
    img_array = imread(image_url)

    return img_array

# Create a function to render an image from the image_url
def render_image(image_url: str):
    # Get extension
    extension = image_url.split('.')[-1]

    # Control Flow to work with GIFs and Static Images
    if extension == 'gif':
        image(image_url)
    else:
        img_array = create_array_from_url(image_url)
        image(img_array)
