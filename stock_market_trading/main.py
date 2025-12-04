import json
import numpy as np
import pandas as pd
import statistics
import requests


tickers = ["NVDA", "AAPL", "TSLA"]
# , 
#     'AMD':df_AMD, 
#     'Berkshire Hathaway':df_BRK, 
#     'DELL':df_DELL, 
#     'EME':df_EME, 
#     'GOOGLE':df_GOOG, 
#     'INTEL':df_INTC, 
#     'NVIDIA':df_NVDA
#     }

all_results = [] #make a list to store results and eventually dump = ["AAPL", "TSLA", "NVDA"]

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

# initial data pull for all stocks!
# for ticker in tickers:
    # initial_data_pull(ticker)


def trim(path):
    # need to remake for the api csv's, they don't have headers
    df = pd.read_csv(path, header=None)
    df.columns = ["Date", "Close/Last"]
# reverse sort the column
    df['Close/Last'] = df['Close/Last'].iloc[::-1].reset_index(drop=True)
# clean up the '$' and round to 2 decimals
    df['Close/Last'] = pd.to_numeric(df['Close/Last'], errors='coerce')
    df['Close/Last'] = df['Close/Last'].round(2)
    return(df)


def append_data():
    pass

def mean_reversion(df):
    prices = []
    #learned this is a more concise way than looping appending to a list
    prices = df['Close/Last'].tolist()
    print(*prices, sep='\n')

    today = 5
    buy = 0
    total_profit = 0
    transactions = 0
    first_buy = 0
    profit = 0
    has_shares = False

    #loop through the list of prices
    for price in prices[5:len(prices)-1]:
        print(f"\nDay {today-4}:")
        #when the price is lower than the reversion threshold, buy a share
        if prices[today] < .98 * statistics.mean(prices[today-5:today]):
            # print(f"previous 5 days' average: {statistics.mean(prices[today-5:today])} or {(prices[today-5] + prices[today-4] + prices[today-3] + prices[today-2] + prices[today-1])/5}")
            # print(prices[today-5], prices[today-4], prices[today-3], prices[today-2], prices[today-1])
            print(f"------------------------------------------------------------------------\nbuying at {prices[today]} because {price} is below the 5 day avg * 0.98 average\n------------------------------------------------------------------------")
            buy = prices[today]
            transactions += 1
            #indicate that we have one share that we could sell
            has_shares = True
            #keep track of the first buy price
            if first_buy == 0:
                first_buy = prices[today]
        #sell a share when the price goes higher than the reversion threshold       
        elif prices[today] > 1.02 * statistics.mean(prices[today-5:today]): 
            #make sure we have a share to buy 
            if first_buy > 0 and has_shares: 
                print(f"------------------------------------------------------------------------\nselling at {prices[today]} because {price} is above the 5 day avg * 1.02\n------------------------------------------------------------------------")
                profit = prices[today] - buy
                #indicate how much we made from the sale
                print(f"trade profit: {round(profit, 2)}")
                total_profit += profit
                transactions += 1
                has_shares = False
            else:
                print("------------------------------------------\n\t***no transaction today***\n------------------------------------------")
            
        else:
            print("------------------------------------------\n\t***no transaction today***\n------------------------------------------")

        today += 1


    # print(f"{company}'s total profit: {round(total_profit, 2)}\nfirst buy: {round(first_buy, 2)}\ntotal return: {round((total_profit/first_buy)*100, 2)}%\ntransactions: {transactions}")

    results = {
        "Strategy":"Mean Reversion",
        # "Company":company,
        "Total Profits":round(total_profit, 2),
        "First Buy":round(first_buy, 2),
        "Total Return Percent":round((total_profit/first_buy)*100, 2),
        "Transactions":transactions
    }

    all_results.append(results)


    with open("/workspaces/DATA_3500_Jefferson_Lund/hw5/results.json", "a") as results_file:
            json.dump(all_results, results_file, indent = 4)


for ticker in tickers:
    mean_reversion(trim(f"/workspaces/DATA_3500_sandbox/stock_market_trading/{ticker}.csv"))

# def simple_moving_average(prices):
#      prices = df['Close/Last'].tolist()
#     # print(*prices, sep='\n')

#     today = 5
#     buy = 0
#     total_profit = 0
#     transactions = 0
#     first_buy = 0
#     profit = 0
#     has_shares = False

#     for price in prices[5:len(prices)-1]:
#         print(f"\nDay {today-4}:")
#         avg_5 = statistics.mean(prices[today-5:today])
        
#         # SMA strategy: buy when price goes above moving average
#         if prices[today] > avg_5:
#             if not has_shares:
#                 print(f"----------------------------------------------------------------\nbuying at {prices[today]} because {price} is above the 5 day avg {avg_5}\n----------------------------------------------------------------")
#                 buy = prices[today]
#                 transactions += 1
#                 has_shares = True
#                 if first_buy == 0:
#                     first_buy = prices[today]
#             else:
#                 print("------------------------------------------\n\t***no transaction today***\n------------------------------------------")

#         # sell when price drops below moving average
#         elif prices[today] < avg_5:
#             if has_shares:
#                 print(f"----------------------------------------------------------------\nselling at {prices[today]} because {price} is below the 5 day avg {avg_5}\n----------------------------------------------------------------")
#                 profit = prices[today] - buy
#                 print(f"trade profit: {round(profit, 2)}")
#                 total_profit += profit
#                 transactions += 1
#                 has_shares = False
#             else:
#                 print("------------------------------------------\n\t***no transaction today***\n------------------------------------------")

#         else:
#             print("------------------------------------------\n\t***no transaction today***\n------------------------------------------")

#         today += 1

#     # print(f"{company}'s total profit: {round(total_profit, 2)}\nfirst buy: {round(first_buy, 2)}\ntotal return: {round((total_profit/first_buy)*100, 2)}%\ntransactions: {transactions}")

#     results = {
#         "Strategy":"Simple Moving Average",
#         "Company":company,
#         "Total Profits":round(total_profit, 2),
#         "First Buy":round(first_buy, 2),
#         "Total Return Percent":round((total_profit/first_buy)*100, 2),
#         "Transactions":transactions
#     }
    
#     all_results.append(results)

