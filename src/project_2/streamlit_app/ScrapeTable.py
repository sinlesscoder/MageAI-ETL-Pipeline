import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

class ScrapeTable:
    """
    Methods:
        - init
        - instantiate_browser
        - run_scraper
        - convert_to_json
    
    """
    def __init__(self, host:str, nav_url: str, xpath: str):
        """
        Arguments:
            - host: Executor URL required to connect to remote Selenium.
            - xpath: Exact XPath required to find the table you want to scrape.
        """
        # Attribute to store the host
        self.host = host

        # Attribute to desired URL to travel to
        self.nav_url = nav_url

        # Attribute to store the XPath
        self.xpath = xpath
    
    def instantiate_browser(self):
        # Creating the Remote Chrome instance as an attribute
        self.browser = webdriver.Remote(command_executor=self.host, desired_capabilities=DesiredCapabilities.CHROME)

    def run_scraper(self):
        # Starting the browser
        self.instantiate_browser()

        # Navigate to desired location
        self.browser.get(self.nav_url)
        
        # Find the table
        self.query = self.browser.find_element(By.XPATH, self.xpath)

        # Create list of results
        self.results = pd.read_html(self.query.get_attribute('innerHTML'))

        return self.results
    
    def convert_to_json(self):
        # Get the results from the scraper
        results = self.run_scraper()

        # Convert DataFrames into dictionaries
        results = [frame.to_dict() for frame in results if isinstance(frame, pd.DataFrame)]

        return json.dumps(results)
    
    def log_postgres(self, table_prefix: str):
        # TODO: Ali's Homework
        pass
        







