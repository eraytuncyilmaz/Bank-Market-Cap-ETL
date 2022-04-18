import requests
import pandas as pd

# EXTRACT DATA USING AN API
# Using ExchangeRate-API we will extract currency exchange rate data.

exchangeratesapi_url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=*******************" # put key here
exchangeratesapi_response = requests.get(exchangeratesapi_url).text

# Using the data gathered turn it into a pandas dataframe.
# The dataframe should have the Currency as the index and Rate as their columns.
# Make sure to drop unnecessary columns.

# Turn the data into a dataframe
rates_df = pd.read_json(exchangeratesapi_response)

# Drop unnecessary columns
rates_df = rates_df[['rates']]

# Save the Dataframe to a csv file
rates_df.to_csv('exchange_rates.csv')