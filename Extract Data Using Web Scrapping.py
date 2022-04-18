from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import wget

# EXTRACT DATA USING WEB SCRAPING
# The wikipedia webpage https://en.wikipedia.org/wiki/List_of_largest_banks provides information about the largest banks in the world by various parameters.
# Scrape the data from the table 'By market capitalization' and store it in a JSON file.


# Webpage Contents
# Gather the contents of the webpage in text format using the requests library and assign it to the variable html_data
wiki_url = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
wiki_response = requests.get(wiki_url)
html_data = wiki_response.text


# Scraping the Data
# Using the contents and beautiful soup load the data from the By market capitalization table into a pandas dataframe.
# The dataframe should have the country Name and Market Cap (US$ Billion) as column names.
# Display the first five rows using head.
soup = BeautifulSoup(html_data, 'html.parser')


# Load the data from the By market capitalization table into a pandas dataframe.
# The dataframe should have the country Name and Market Cap (US$ Billion) as column names.
# Using the empty dataframe data and the given loop extract the necessary data from each row and append it to the empty dataframe.
bank_df = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])

for row in soup.find_all('tbody')[3].find_all('tr'):
    col = row.find_all('td')
    if len(col) > 0:
        name = col[1].text.strip()
        market_cap = float(col[2].string.strip())
        bank_df = bank_df.append({"Name": name, "Market Cap (US$ Billion)": market_cap}, ignore_index=True)


# Create JSON dump
js = bank_df.to_json(orient='columns')


# Store the JSON dump to a file
with open('bank_market_cap.json', 'w') as outfile:  # writing JSON object
    outfile.write(js)