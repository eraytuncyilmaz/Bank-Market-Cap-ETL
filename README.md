# Bank-Market-Cap-ETL
Creating ETL for extracting the list of the largest banks by market capitalization (in USD) using webscrapping and extracting currency exchange rates using APIs.  
Transform from USD to EUR and save the transformed data in a ready-to-load format
<br/>

## Data Description
• Extract the list of the largest banks by market capitalization data from https://en.wikipedia.org/wiki/List_of_largest_banks  
• Extract currency exchange rates data from https://exchangeratesapi.io/  
<br/>

## Project Tasks
• Run the ETL process  
• Extract bank market cap data from the JSON file, bank_market_cap.json  
• Extract exchange rates data from the csv file, exchange_rates.csv  
• Transform the market cap currency using the exchange rate data  
• Load the transformed data into a seperate CSV, bank_market_cap_eur.csv