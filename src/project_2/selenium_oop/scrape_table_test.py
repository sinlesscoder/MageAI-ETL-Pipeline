from ScrapeTable import ScrapeTable

# Run for example XPath
scraper = ScrapeTable('http://209.182.236.218:4445',
                       nav_url="https://en.wikipedia.org/wiki/Comparison_of_programming_languages",
                       xpath="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]")

# Convert results to JSON file
scraper.convert_to_json('sample_results.json')