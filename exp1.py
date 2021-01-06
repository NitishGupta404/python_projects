import  json
import requests

r=requests.get("https://financialmodelingprep.com/api/v3/quotes/nse?apikey=7abf233d6d4bf7ee15b4e67b27f9761e").text

stockdata=json.loads(r)

stocklist=["TOKYOPLAST.NS","KNRCON.NS","JPPOWER.NS"]

for stock in stocklist:
    for item in stockdata:
        if stock in item['symbol']:
            print(stock)
            print(item['price'])
            break
