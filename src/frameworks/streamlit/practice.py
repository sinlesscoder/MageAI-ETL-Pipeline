import streamlit as st
import pandas as pd

data = [
    ['John', 25, 'New York', '/home/aahmed/Pathrise_Ali_Data_Tutorials/src/frameworks/streamlit/new-york-city-evening-NYCTG0221-52492d6ccab44f328a1c89f41ac02aea.jpg'],
    ['Emma', 28, 'London', '/home/aahmed/Pathrise_Ali_Data_Tutorials/src/frameworks/streamlit/fb95eca49cf3f2af57455b1358f1ec39193ce256.webp'],
    ['Tom', 32, 'Paris', '/home/aahmed/Pathrise_Ali_Data_Tutorials/src/frameworks/streamlit/france-eiffel-tower-paris.jpg']
]

st.markdown("<h1 style='text-align:center'>Social Profile App </h1>", unsafe_allow_html=True)

for i in range(len(data)):
    for j in range(len(data[i])):
        if j == 0:
            st.markdown("<h3>Name: </h3>", unsafe_allow_html=True)
            user_name = st.markdown(data[i][j], unsafe_allow_html=True)
        if j == 1:
            st.markdown("<h3>Age: </h3>", unsafe_allow_html=True)
            age = st.markdown(data[i][j], unsafe_allow_html=True)
        if j == 2:
            st.markdown("<h3>Area: </h3>", unsafe_allow_html=True)
            area = st.markdown(data[i][j], unsafe_allow_html=True)
        if j ==3:
            left_column,right_column=st.columns(2)
            with left_column:
                st.image(data[i][j],caption='Image Caption')
    st.write("---")   
    st.write("##")



