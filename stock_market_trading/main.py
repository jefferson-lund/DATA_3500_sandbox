import requests
import json

tickers = ["AAPL", "TSLA", "NVDA"]
# , "SONY", "COST", "META", "AMZN", "SNAP", "DAL", "FIX"]

def initial_data_pull(ticker):
    # keys
    key1 = "Time Series (Daily)"
    key2 = "4. close"
    # date_key = "" # I know I need all the dates (maybe use an iterator variable?  ??)

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

    request = requests.get(url)
    request_dictionary = json.loads(request.text)
    # print(request_dictiona    r   y)


    file = open(f"/workspaces/DATA_3500_sandbox/stock_market_trading/{ticker}.csv", "w")

    lines =  []

    for date in request_dictionary[key1].keys():
        lines.append(date + ", " + request_dictionary[key1][date][key2] + "\n")

    lines = lines[::-1]
    file.writelines(lines)
    file.close()

for ticker in tickers:
    initial_data_pull(ticker)