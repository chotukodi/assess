import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_nse_data():
    url = 'https://www1.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'top10_gainers_loser'})
        
        if table:
            rows = table.find_all('tr')[2:]  # Skip the header rows
            
            data = []
            for row in rows:
                columns = row.find_all('td')
                symbol = columns[0].text.strip()
                ltp = float(columns[1].text.strip().replace(',', ''))
                change = float(columns[2].text.strip().replace(',', ''))
                
                data.append({
                    'Symbol': symbol,
                    'LTP': ltp,
                    'Change': change
                })
            
            df = pd.DataFrame(data)
            return df
        else:
            print('Table not found on the webpage.')
    else:
        print(f'Request failed with status code: {response.status_code}')

nse_data = scrape_nse_data()
if nse_data:
    print('NSE Top Gainers:')
    print(nse_data)
else:
    print('Failed to scrape NSE data.')
