import streamlit as st
from ScrapeTable import ScrapeTable

# Centered Title
st.markdown("<h1 style='text-align:center'> Table Scraper Application </h1>", unsafe_allow_html=True)

# Description
st.markdown("<p 'text-align:center'> This application allows an end user to choose an XPath and a URL where a table exists to get the data in the form of JSON. </p>", unsafe_allow_html=True)

# URL to the site
site_url = st.text_input("Type in the URL you want to scrape at: ")

# Retrieve the XPath to the table you want
table_xpath = st.text_input("Paste your full table XPath: ")

# Button to scrape
if st.button("Scrape"):
    # Start up the scraper
    scraper = ScrapeTable('http://209.182.236.218:4445', site_url, table_xpath)

    # JSON string
    json_str = scraper.convert_to_json()

    # Download
    st.download_button(
        label="Retrieve your results here:",
        data=json_str.encode(),
        file_name='results.json',
        mime='application/json'
    )



