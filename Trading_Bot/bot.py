import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# # Works

# #Get Apple stock Historical data
# data = yf.download('aapl','2018-01-01')
# #Plot the Close price
# data.Close.plot()
# plt.show()

# #Print the Close price
# print(data.Close)

# #Print the Open price
# print(data.Open)


### Apple Stock ###

aapl = yf.Ticker("AAPL")

# # get stock info
# print(aapl.info)

# # get historical market data
# hist = aapl.history(period="max")
# print(hist)

# # show actions (dividends, splits)
# print(aapl.actions)

# # show dividends
# aapl.dividends

# # show splits
# aapl.splits

# # show financials
# aapl.financials
# aapl.quarterly_financials

# # show major holders
# stock.major_holders

# # show institutional holders
# stock.institutional_holders

# # show balance heet
# aapl.balance_sheet
# aapl.quarterly_balance_sheet

# # show cashflow
# aapl.cashflow
# aapl.quarterly_cashflow

# # show earnings
# aapl.earnings
# aapl.quarterly_earnings

# # show sustainability
# aapl.sustainability

# # show analysts recommendations
# aapl.recommendations

# # show next event (earnings, etc)
# aapl.calendar

# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# aapl.isin

# # show options expirations
# aapl.options

# # get option chain for specific expiration
# opt = aapl.option_chain('YYYY-MM-DD')
# # data available via: opt.calls, opt.puts

# # Don't work

