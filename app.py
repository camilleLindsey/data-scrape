#this is number 3
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
web_page = [
    'https://finance.yahoo.com/quote/FB?p=FB', 'https://finance.yahoo.com/quote/AAPL?p=AAPL']

data = []

for page in web_page:
    co_pg = urllib2.urlopen(page)
    soup = BeautifulSoup(co_pg, 'html.parser')
    name_box = soup.find('h1', attrs={'class': 'D(ib)'})
    name = name_box.text
    print(name)

    price_box = soup.find('span', attrs={'class': 'Fw(b)'})
    price=price_box.text
    print(price)
    data.append((name, price))

with open('data.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
        writer.writerow([name, price, datetime.now()])









#this is number 1 
# import urllib2
# from bs4 import BeautifulSoup

# #1  getting web page:
# web_page = 'https://finance.yahoo.com/quote/FB?p=FB'
# web_page = 'https://finance.yahoo.com/quote/COST?p=COST'
# web_page = 'https://finance.yahoo.com/quote/^RUT?p=^RUT'
# web_page = 'https://finance.yahoo.com/quote/BRKB?p=BRKB'
# #query the website and return the html to the variable page:
# page = urllib2.urlopen(web_page)

# #print(page)


# soup = BeautifulSoup(page, 'html.parser')

# #soup + BeautifulSoup(page.text, 'html.parser')

# name_box = soup.find('h1', attrs={'class': 'D(ib)'})

# #print(name_box)
# name = name_box.text
# print(name)
# # print (name_box)
# # name = name_box.text
# # print(name)
# price_box = soup.find('span', attrs={'class': 'Fw(b)'})
# price = price_box.text
# print(price)

# import csv
# from datetime import datetime

# #with open('index.csv', 'w') as csv_file: #write
# with open('index.csv', 'a') as csv_file: #append

#     writer = csv.writer(csv_file) 
#     writer.writerow([name, price, datetime.now()])

# input = 0
# while input < 10:
#     print(input)
#     input += 1