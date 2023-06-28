import streamlit as st
import pandas as pd

data = [
    ['John', 25, 'New York', '/home/aahmed/Pathrise_Ali_Data_Tutorials/src/frameworks/streamlit/new-york-new-york-city.gif'],
    ['Emma', 28, 'London', '/home/aahmed/Pathrise_Ali_Data_Tutorials/src/frameworks/streamlit/fb95eca49cf3f2af57455b1358f1ec39193ce256.webp'],
    ['Tom', 32, 'Paris', '/home/aahmed/Pathrise_Ali_Data_Tutorials/src/frameworks/streamlit/france-eiffel-tower-paris.jpg']
]

john = {'name': 'John', 'age': 25, 'Area': 'New York', 'Image': '/home/aahmed/Pathrise_Ali_Data_Tutorials/src/frameworks/streamlit/new-york-new-york-city.gif'}
emma = {'name': 'Emma', 'age': 28, 'Area': 'New York', 'Image': '/home/aahmed/Pathrise_Ali_Data_Tutorials/src/frameworks/streamlit/new-york-new-york-city.gif'}

st.markdown("<h1 style='text-align:center'>Social Profile App </h1>", unsafe_allow_html=True)

# Add some text components
user_name = st.text_input("Type in a username: ")

# Add some information about yourself
user_bio = st.text_area("Describe yourself: ", max_chars=1000)

# Upload a profile photo
uploaded_image= st.file_uploader("Upload a profile photo: ", type=['png', 'jpg'])

# Upload button
if st.button('Upload'):
    # Create the actual preview
    st.markdown(f"<h2 style='text-align:center'> Welcome, {user_name} </h2>", unsafe_allow_html=True)
    st.markdown(f"<p> {user_bio} </p>", unsafe_allow_html=True)
    st.image(uploaded_image, use_column_width=True)

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



