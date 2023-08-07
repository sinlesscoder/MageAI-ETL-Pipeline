import streamlit as st

class Form:
    def __init__(self, n):
        self.n = n
        self.values = []
    # Create inputs
    def create_inputs(self):
        for i in range(self.n):
            imp = st.text_input("This is an input", key=f'input_{i}')
            self.values.append(imp)
    # Submit Button
    def submit(self):
        if st.button('Submit'):
            st.write("\n".join(self.values))
    
    # Construct
    def construct(self):
        self.create_inputs()
        self.submit()

class DataFrameView:
    # def __init__(self, df):
    #     self.df = df

    def view_frame(self, df):
        st.dataframe(df, use_container_width=True)
