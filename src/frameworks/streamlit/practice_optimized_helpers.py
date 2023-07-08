import pandas as pd
from streamlit import image
from sqlalchemy import create_engine
from skimage.io import imread

# Create the data object as a function
def create_object(name, age, area, image_url):
    result = {
        'name' : name,
        'age': age,
        'area': area,
        'image': image_url
    }

    return result

# Convert data list to pandas DataFrame
def create_df_from_objects(data_list):
    # Get the dictionary keys
    keys = list(data_list[0].keys())

    # Create an empty dictionary
    result_dict = {key : [] for key in keys}

    for obj in data_list:
        for key in keys:
            # Transform into dictionary with lists of similar keys in each
            result_dict[key].append(obj[key])
    
    # Convert to pandas DataFrame
    return pd.DataFrame.from_dict(result_dict)

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

# Function to turn DataFrame into SQL table in duckDB
def create_duckdb_sql_table(data):
    # Upload the data to pandas DataFrame
    result_df = create_df_from_objects(data)

    # Create duckdb connection
    duckdb_con = duckdb_connection('results.db')

    # Export the DataFrame to a DuckDB table
    result_df.to_sql('results', con=duckdb_con, index=False, if_exists='append')

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
