import streamlit as st

class StringDropdown:
    def __init__(self, docs: list, key: str, id: int):
        self.docs = docs
        self.column = key
        self.id = id
    
    def create_dropdown(self, collector: list):
        # Unique values for the key
        unique_values = list(set([doc[self.column] for doc in self.docs]))

        # Create a dropdown
        self.dropdown = st.selectbox(f"Select an option for column: {self.column}:", options=unique_values, key=self.id)

        collector.append({self.column : self.dropdown})

