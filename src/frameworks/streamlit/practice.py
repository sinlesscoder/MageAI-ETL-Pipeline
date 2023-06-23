import streamlit as st
import pandas as pd

data = [
    ['John', 25, 'New York'],
    ['Emma', 28, 'London'],
    ['Tom', 32, 'Paris']
]

st.markdown("<h1 style='text-align:center'>Social Profile App </h1>", unsafe_allow_html=True)

for i in range(len(data)):
    for j in range(len(data[i])):
        if j == 0:
            st.markdown("<h3>Username: </h3>", unsafe_allow_html=True)
            user_name = st.markdown(data[i][j], unsafe_allow_html=True)
        if j == 1:
            st.markdown("<h3>Age: </h3>", unsafe_allow_html=True)
            age = st.markdown(data[i][j], unsafe_allow_html=True)
        if j == 2:
            st.markdown("<h3>Area: </h3>", unsafe_allow_html=True)
            area = st.markdown(data[i][j], unsafe_allow_html=True)
    st.markdown("<h3>----------------------------------</h3>", unsafe_allow_html=True)


