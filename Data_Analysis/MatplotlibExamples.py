import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dataset.csv')
#print(data)
#print(data.describe())
df = pd.DataFrame(data)
'''
plt.figure(figsize=(8, 4))
sns.histplot(df['Price'], bins=5, color='green')
plt.title('Price Distribution')
plt.xlabel('Price: ')
plt.ylabel('Frequency')
#plt.show()
'''
'''
#Price vs Rating
plt.figure(figsize=(8,6))
sns.scatterplot(x='Price', y='Rating', data=df, sizes=(50, 200))
plt.title('Price vs rating')
plt.xlabel('Rs.')
plt.ylabel('Rating')
plt.show()
'''
'''
plt.figure(figsize=(8, 6))
plt.bar(data=df, x='Price', height=10)
plt.xlabel('')
plt.show()
'''
'''
data1 = ['Player1', 'Player2', 'Player3']
values = [30, 45, 25]
plt.figure(figsize=(4,2))
#plt.pie(values, labels=data1)
plt.bar(data1, values, width=0.1)
plt.xlabel('Players')
plt.ylabel('Scores')
plt.show()
'''
apple_stock = yf.download('AAPL', start='2024-01-01', end='2024-10-01')
ms_stock = yf.download('MSFT', start='2024-01-01', end='2024-10-01')

plt.plot(apple_stock.index, apple_stock['Close'], label='Apple', marker='o')
plt.plot(ms_stock.index, ms_stock['Close'], label='Microsoft', marker='s')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock prices of the S/W Companies')
plt.legend()
plt.show()