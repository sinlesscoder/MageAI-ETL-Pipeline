import streamlit as st
from StringDropdown import StringDropdown
from NumberDropdown import NumberDropdown
from mongo_db import connect_mongo
from key_value_mapper import kvmapper
from json_cache import result_serialize, read_json

mongo_uri = "mongodb://209.182.236.218:8975"
db = 'sample_db'

mongo_db = connect_mongo(mongo_uri, db)

# # Try with sample collection
# sample = mongo_db['stock_market']

# Title
st.title("Hello Streamlit")

# Setup a filter collector
filter_collector = []

# Helper Function
# def view_widgets(updated_kv, sample_docs, filter_collector):
    
# Collection to work with
col_choice = st.selectbox("Choose a MongoDB collection to work with: ", options=['stock_market', 'spotify_tracks', 'sample'])
sample = mongo_db[col_choice]

# Key Value Mapping
# Sample documents
sample_docs = [doc for doc in sample.find()]

# Apply kvmapper
kv_mapped = kvmapper(sample_docs)

# Define updated_kv as kv_mapped
updated_kv = read_json()

# Cols to Select
chosen_keys = st.multiselect("Choose columns you want to query: ", list(kv_mapped.keys()))

# Modify button
if st.button("Modify"):
    updated_kv = {k:v for k,v in kv_mapped.items() if k in chosen_keys}
    result_serialize(updated_kv)
    widget_state = True

    
with st.expander("Expand to view your results: ", expanded=True):
    # Create logic to build the widgets
    for i, key in enumerate(updated_kv):
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





# # row_column creator
# def row_col_creator(kv_dict: dict, num_cols: int):
#     # Row cols
#     row_cols = []

#     # Number of keys
#     num_keys = len(kv_dict)

#     # Integer division
#     num_rows = num_keys / num_cols

#     # List of row objects
#     for row in range(num_rows):
#         row_results = []
#         # Get the columns
#         col_list = st.columns(num_cols, gap='medium')
#         col_container_dict = {f'col_{i+1}' : cont for i, cont in enumerate(col_list)}
    
#         row_cols.append(col_container_dict)
    
#     return row_cols


