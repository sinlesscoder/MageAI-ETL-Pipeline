import streamlit as st
from StringDropdown import StringDropdown
from NumberDropdown import NumberDropdown
from mongo_db import connect_mongo
from key_value_mapper import kvmapper

mongo_uri = "mongodb://209.182.236.218:8975"
db = 'sample_db'

mongo_db = connect_mongo(mongo_uri, db)

# Try with sample collection
sample = mongo_db['stock_market']

# Title
st.title("Hello Streamlit")

# Setup a filter collector
filter_collector = []

# Sample documents
sample_docs = [doc for doc in sample.find()]

# Apply kvmapper
kv_mapped = kvmapper(sample_docs)

# row_column creator
def row_col_creator(kv_dict: dict, num_cols: int):
    # Row cols
    row_cols = []

    # Number of keys
    num_keys = len(kv_dict)

    # Integer division
    num_rows = num_keys / num_cols

    # List of row objects
    for row in range(num_rows):
        row_results = []
        # Get the columns
        col_list = st.columns(num_cols, gap='medium')
        col_container_dict = {f'col_{i+1}' : cont for i, cont in enumerate(col_list)}
    
        row_cols.append(col_container_dict)
    
    return row_cols



# Create logic to build the widgets
for i, key in enumerate(kv_mapped):
    # Build widget based on type
    if kv_mapped[key] == 'number':
        # Numerical Widget
        widget = NumberDropdown(sample_docs, key, i)
    elif kv_mapped[key] == 'string':
        # String Widget
        widget = StringDropdown(sample_docs, key, i)
    
    widget.create_dropdown(filter_collector)

# Button
if st.button("View sub-filters"):
    st.json(filter_collector)



