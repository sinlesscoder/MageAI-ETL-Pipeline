import streamlit as st

# Social Profile App
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
