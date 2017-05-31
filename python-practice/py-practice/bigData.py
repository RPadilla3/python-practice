import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

start = datetime.datetime(2001, 1, 1)
end = datetime.datetime(2016, 1, 1)

df = web.DataReader('XOM', 'yahoo', start, end)

print(df.head())

df['Adj Close'].plot()

plt.show()
