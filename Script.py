import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")


#print(API_KEY)
LIMIT = 100
url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={API_KEY}"
requestsdata = requests.get(url)
#print(requestsdata.json())

tickers = []


data = requestsdata.json()
print(data.keys())
for ticker in data['results']:
        tickers.append(ticker)


while 'next_url' in data:
    print('requesting next url', data['next_url'])
    response = requests.get(data['next_url']+ f'&apiKey={API_KEY}')
    data = response.json()
    for ticker in data['results']:
        tickers.append(ticker)
    
print(len(tickers))
