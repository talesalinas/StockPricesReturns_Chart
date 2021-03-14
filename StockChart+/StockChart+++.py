import pandas 
from pandas_datareader import data as web
import numpy 
import matplotlib.pyplot as plt 

Stocks = []
while True:
    ticker = input('Ticker: ').upper().strip()
    Stocks.append(ticker)
    newstock = ''
    while newstock != 'Y' and newstock != 'N':
        newstock = input('Do you want to add another stock? ').upper().strip()[0]
    if newstock == 'N':
        break

MyTickers = pandas.DataFrame()
for stock in Stocks:
    MyTickers[stock] = web.DataReader(stock, 'yahoo', start='2011-01-01')['Adj Close']
MyStocks = MyTickers.reset_index() # You can reset the data frame, so you'll have an column only for the dates. #

# THIS IS ONLY THE BASIC PRICE CHART OF ALL THE STOCKS #

#for t in Stocks:
    #plt.plot(MyStocks['Date'], MyStocks[t]) *This is another way of making the chart*
MyTickers.plot(figsize=(12,6))
plt.ylabel('price')
plt.xlabel('Date')

# NOW, THIS IS THE PRICE CHART OF THE STOCKS, BUT SHOWING HOW THEY WOULD HAVE PERFORMED DURING THE PERIOD, IF THEY ALL HAVE STARTED WITH A $100.00 DOLLAR PRICE #

(MyTickers / MyTickers.iloc[0] * 100).plot(figsize=(12,6))
plt.show()

# THIS IS THE DAILY % RETURN OF ALL THE STOCKS #

DailyReturns = pandas.DataFrame()
for s in Stocks:
    DailyReturns[s] = round(((MyTickers[s] / MyTickers[s].shift(1)) - 1) * 100, 2)
    print(f'{s} average daily return: {round(DailyReturns[s].mean(), 4)}%')
    print(f'{s} average anual returns: {round(DailyReturns[s].mean() * 250, 4)}%') # 250 working days #
DailyReturns.plot(figsize=(12,6))

plt.show()
