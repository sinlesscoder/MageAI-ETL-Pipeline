import numpy as np
import pandas as pd
import streamlit as st
from widget_classes import Form, DataFrameView

class App(Form, DataFrameView):
    # Method: Build Entire App
    def build_app(self, title):
        st.title(title)

        self.construct()

        st.success("Your app has successfully been built.")

# Create the app

## Create random dataframe
df = pd.DataFrame(np.random.randint(0, 100, size=(5000, 10)))

app = App(3)

app.build_app('My App')

app.view_frame(df)
