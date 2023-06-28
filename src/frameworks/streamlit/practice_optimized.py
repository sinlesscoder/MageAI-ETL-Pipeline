import duckdb
import duckdb_engine
import pandas as pd
import streamlit as st
from os import getcwd
from sqlalchemy import create_engine


# Create the data object as a function
def create_object(name, age, area, image):
    result = {
        'name' : name,
        'age': age,
        'area': area,
        'image': image
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

    return con

data = [
    create_object('John', 25, 'New York', f'{getcwd()}/new-york-new-york-city.gif'),
    create_object('Emma', 28, 'London', f'{getcwd()}/fb95eca49cf3f2af57455b1358f1ec39193ce256.webp'),
    create_object('Tom', 32, 'Paris', f'{getcwd()}/france-eiffel-tower-paris.jpg')
]

# Function to turn DataFrame into SQL table in duckDB
def create_duckdb_sql_table(data):
    # Upload the data to pandas DataFrame
    result_df = create_df_from_objects(data)

    # Create duckdb connection
    duckdb_con = duckdb_connection('results.db')

    # Export the DataFrame to a DuckDB table
    result_df.to_sql('results', con=duckdb_con, index=False, if_exists='append')

st.markdown("<h1 style='text-align:center'>Social Profile App </h1>", unsafe_allow_html=True)

# Add some text components
user_name = st.text_input("Type in a name: ")

# Add a number input for age
user_age = st.number_input('Type in your age: ', min_value=1, max_value=200, value=16)

# Add some information about yourself
user_area = st.text_input("Type in an area: ")

# Upload a profile photo
uploaded_image= st.file_uploader("Upload an image: ", type=['png', 'jpg', 'webp', 'gif', 'jpeg'])

# Upload button
if st.button('Upload'):
    # Add to the data list
    new_result = create_object(user_name, user_age, user_area, uploaded_image)
    data.append(new_result)
    # Add to the DuckDB SQL table
    create_duckdb_sql_table(data)

# Loop through each data object
for obj in data:
    # Format the entities using h3 tags and view the image with the column positions
    st.markdown("<h3>Name: </h3>", unsafe_allow_html=True)
    user_name = st.markdown(obj['name'], unsafe_allow_html=True)
    st.markdown("<h3>Age: </h3>", unsafe_allow_html=True)
    age = st.markdown(obj['age'], unsafe_allow_html=True)
    st.markdown("<h3>Area: </h3>", unsafe_allow_html=True)
    area = st.markdown(obj['area'], unsafe_allow_html=True)
    left_column,right_column=st.columns(2)
    with left_column:
        st.image(obj['image'],caption='Image Caption')
    st.write("---")   
    st.write("##")



