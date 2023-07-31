import streamlit as st
from StringDropdown import StringDropdown
from NumberDropdown import NumberDropdown
from mongo_db import connect_mongo
from key_value_mapper import kvmapper

mongo_uri = "mongodb://209.182.236.218:8975"
db = 'sample_db'

mongo_db = connect_mongo(mongo_uri, db)

# Try with sample collection
sample = mongo_db['stock_sample']

# Title
st.title("Hello Streamlit")

# Setup a filter collector
filter_collector = []

# Sample documents
sample_docs = [doc for doc in sample.find()]

# Apply kvmapper
kv_mapped = kvmapper(sample_docs)

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



