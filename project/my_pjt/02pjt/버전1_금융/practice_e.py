import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = 'archive/NFLX.csv'
df = pd.read_csv(csv_path, usecols=range(0, 5))

df['Date'] = pd.to_datetime(df['Date'])
df_2022 = df[df['Date'] >= '2022']

plt.plot(df_2022['Date'], df_2022['High'], label="High")
plt.plot(df_2022['Date'], df_2022['Low'], label="Low")
plt.plot(df_2022['Date'], df_2022['Close'], label="Close")

plt.title('High, Low, and Close Prices since January 2022')
plt.xlabel('Date')
plt.ylabel('Price')

# x축 회전
plt.xticks(rotation=45)

plt.legend()
plt.show()