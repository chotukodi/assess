import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_crypto_prices():
    url = 'https://coinmarketcap.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        crypto_table = soup.find('table', {'id': 'cryptocurrencies'})
        
        if crypto_table:
            cryptocurrencies = []
            
            # Find all rows in the table, skipping the header row
            rows = crypto_table.find_all('tr')[1:]
            
            for row in rows:
                # Extract the data from each column in the row
                columns = row.find_all('td')
                rank = int(columns[0].text.strip())
                name = columns[1].text.strip()
                price = float(columns[3].text.strip().replace('$', '').replace(',', ''))
                market_cap = float(columns[4].text.strip().replace('$', '').replace(',', ''))
                
                # Create a dictionary with the extracted data
                crypto_data = {
                    'Rank': rank,
                    'Name': name,
                    'Price': price,
                    'Market Cap': market_cap
                }
                cryptocurrencies.append(crypto_data)
            
            # Create a pandas DataFrame from the scraped data
            df = pd.DataFrame(cryptocurrencies)
            return df
        else:
            print('Cryptocurrency table not found on the webpage.')
    else:
        print(f'Request failed with status code: {response.status_code}')

# Run the web scraping in a loop to get real-time data every few seconds
while True:
    crypto_data = scrape_crypto_prices()
    
    if crypto_data:
        print('Cryptocurrency Prices:')
        print(crypto_data)
    else:
        print('Failed to scrape cryptocurrency prices.')
    
    # Wait for a few seconds before the next scrape
    time.sleep(5)