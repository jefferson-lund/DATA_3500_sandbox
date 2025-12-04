# MTS Table 1 API - JSON Format
# Import necessary packages
import requests
import pandas as pd
import json
import csv
# Create API variables
baseUrl = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'
endpoint = '/v1/accounting/dts/deposits_withdrawals_operating_cash'
fields = ''
filter = ''
sort = ''
format = ''
pagination = ''
API = f'{baseUrl}{endpoint}{fields}{filter}{sort}{format}{pagination}'
# Call API and load into a pandas dataframe
data = requests.get(API)
data_dictionary = json.loads(data.text)

with open("/workspaces/DATA_3500_Jefferson_Lund/FinalProject/json_dump.json", "w") as file:
    json.dump(data_dictionary["data"], file, indent=4)

fieldnames = data_dictionary["data"][0].keys()
with open ("/workspaces/DATA_3500_Jefferson_Lund/FinalProject/api_data.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_dictionary["data"])

df = pd.read_csv("/workspaces/DATA_3500_Jefferson_Lund/FinalProject/api_data.csv")
df.drop(columns=["record_fiscal_year", "record_fiscal_quarter", "record_calendar_year", "record_calendar_quarter", "record_calendar_month", "record_calendar_day", "table_nbr", "table_nm"], inplace=True)
df.to_csv("/workspaces/DATA_3500_Jefferson_Lund/FinalProject/api_data.csv")

