import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

# Remote Selenium
browser = webdriver.Remote('http://209.182.236.218:4445', desired_capabilities=DesiredCapabilities.CHROME, keep_alive=False)

# browser = webdriver.Chrome()

# Navigate to wikipedia page with some table
browser.get("https://en.wikipedia.org/wiki/Comparison_of_programming_languages")

# Extract the table
table_to_extract = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]")

# Read HTML table into pandas
df = pd.read_html(table_to_extract.get_attribute('innerHTML'))

print(df[1].head())