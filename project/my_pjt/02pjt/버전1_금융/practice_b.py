import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = 'archive/NFLX.csv'
df = pd.read_csv(csv_path, usecols=range(0, 5))

df['Date'] = pd.to_datetime(df['Date'])
df_2021 = df[df['Date'] >= '2021']

plt.plot(df_2021['Date'], df_2021['Close'])

plt.title('NFLX Close Price')
plt.xlabel('Date')
plt.ylabel('Close Price')

# x축 회전
plt.xticks(rotation=45)

plt.show()
