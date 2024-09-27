import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = 'archive/NFLX.csv'
df = pd.read_csv(csv_path, usecols=range(0, 5))

df['Date'] = pd.to_datetime(df['Date'])
df_2021 = df[df['Date'] >= '2021']

df_2021['month'] = df_2021['Date'].dt.to_period('M')
monthly_avg = df_2021.groupby('month')['Close'].mean()
monthly_avg.index = monthly_avg.index.to_timestamp()

plt.plot(monthly_avg.index, monthly_avg)

plt.title('Monthly Average Close Price')
plt.xlabel('Date')
plt.ylabel('Average Close Price')

# x축 회전
plt.xticks(rotation=45)
plt.show()