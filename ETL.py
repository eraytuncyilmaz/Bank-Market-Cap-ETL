import glob
import pandas as pd
from datetime import datetime


# EXTRACT
# JSON Extract Function
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe


# Store the data in a pandas dataframe. Use the following list for the columns
columns = ['Name', 'Market Cap (US$ Billion)']


def extract():
    dataframe = pd.DataFrame(columns=columns)  # create an empty data frame to hold extracted data, columns are defined previously

    # process all JSON files
    for jsonfile in glob.glob('*.json'):  # In this case there is only one JSON file, bank_market_cap
        dataframe = dataframe.append(extract_from_json(jsonfile), ignore_index=True)  # Append all the data coming from JSON files

    return dataframe


# Load the file exchange_rates.csv as a dataframe and find the exchange rate for USD, store it in the variable exchange_rate
df = pd.read_csv('exchange_rates.csv', index_col=0)
EUR_to_USD = df.loc['USD', 'rates']
USD_to_EUR = 1 / EUR_to_USD


# TRANSFORM
# Changes the Market Cap (US$ Billion) column from USD to EUR
# Rounds the Market Cap (US$ Billion)` column to 3 decimal places
# Rename Market Cap (US$ Billion) to Market Cap (EUR$ Billion)

def transform(df):
    # Write your code here
    transformed_df = df.copy()
    transformed_df['Market Cap (US$ Billion)'] = round(USD_to_EUR * transformed_df['Market Cap (US$ Billion)'], 3)
    transformed_df.rename(columns={'Market Cap (US$ Billion)': 'Market Cap (EUR$ Billion)'}, inplace=True)
    return transformed_df


# LOAD
def load(data):
    # Write your code here
    targetfile = 'bank_market_cap_eur.csv'
    data.to_csv(targetfile, index=False)


# Logging Function
def log(message):
    # Write your code here
    timestamp_format = '%Y-%h-%d-%H:%M:%S'  # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt", "a") as f:
        f.write(timestamp + ',' + message + '\n')


# RUNNING ETL PROCESS
log("ETL Job Started")
log("Extract phase Started")
extracted_df = extract()
#print(extracted_df.head())
log("Extract phase Ended")

log("Transform phase Started")
transformed_df = transform(extracted_df)
#print(transformed_df.head())
log("Transform phase Ended")

log("Load phase Started")
load(transformed_df)
log("Load phase Ended")
