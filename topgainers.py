from bs4 import BeautifulSoup
import requests
import json

link3="https://www.moneycontrol.com/stocks/marketstats/nsegainer/index.php"
source=requests.get(link3).text

soup=BeautifulSoup(source ,'lxml')
company=[]
actualcompanyname=[]
company_for_search=[]
rawdata=soup.find('div' , class_='bsr_table hist_tbl_hm')
rawcompany=rawdata.find('tbody')
rawcompany1=rawcompany.find_all('td' ,class_='PR')
for item in rawcompany1:
    company.append(item.a['href'])

for c in company:
    r=requests.get(c).text
    soup2=BeautifulSoup(r,'lxml')
    data1=soup2.find('div' , class_='inid_name')
    companyname=data1.h1.text
    actualcompanyname.append(companyname)

print(len(actualcompanyname))
for i in actualcompanyname:
    if 'Ltd. ' in i:
        var=i.replace('Ltd. ' ,'Limited')
        company_for_search.append(var)
    else:
        company_for_search.append(i.strip())
k=requests.get("https://financialmodelingprep.com/api/v3/quotes/nse?apikey=7abf233d6d4bf7ee15b4e67b27f9761e").text
stockdata=json.loads(k)
for stock in company_for_search:
    for item2 in stockdata:
        if stock in item2['name']:
            print(stock)
            print(item2['price'])
            break









