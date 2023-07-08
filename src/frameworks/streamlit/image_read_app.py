import streamlit as st
from skimage.io import imread

# Paste an image URL
image_url = st.text_input("Paste an image URL: ")

# Retrieve array function
def retrieve_array(url):
    return imread(url)

# Create a button
if st.button("View"):
    # Get the array of the URL passed as input into Streamlit
    img = retrieve_array(image_url)

    # REnder the image using st.image
    st.image(img)