import numpy as np 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données de dassault depuis 2015

data_bank = yf.download("DSY.PA", start="2015-01-01", end="2024-12-31")
data_bank.to_excel("action_dassault_system.xlsx")
print (data_bank.head())
close_prices = data_bank[('Close','DSY.PA')]
open_prices =  data_bank[('Open','DSY.PA')]
diff_prices = close_prices - open_prices
dates = data_bank.index
plt.plot(dates,open_prices)

plt.plot(dates,diff_prices)
plt.title('différences entre prix douverture et de cloture')

plt.show()

