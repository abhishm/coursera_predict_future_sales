from itertools import product
import datetime
import pandas as pd
from forex_python.converter import CurrencyRates

c = CurrencyRates()
years = [2013, 2014, 2015]
months = range(1, 13)
years, months = list(zip(*product(years, months)))

rates = []
for year, month in zip(years, months):
    date = datetime.datetime(year, month, 15) 
    # taking the middle of month as the proxy rates
    rate = c.get_rate("USD", "RUB", date)
    rates.append(rate)
        
df = pd.DataFrame({"year": years, "month": months, "rates": rates})
df.to_csv("../data/conversion_rates.csv", index=False)