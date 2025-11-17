
import json
import requests
import pandas as pd

# keys
date_key = "" #I know I need all the dates at some point maybe use iterator?
key1 = "Time Series (Daily)"
key2 = "#4. close"
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

request = requests.get(url)
request_list = request.text
request_dict = json.loads(request.text)
print(request_dict)
# with open("/workspaces/DATA_3500_sandbox/stock_market_trading/AAPL.csv", "w") as f:

#     for date in request_dict[key1].keys():
#         f.write()        
