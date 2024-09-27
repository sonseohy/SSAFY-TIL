import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = 'archive/NFLX.csv'
df = pd.read_csv(csv_path, usecols=range(0, 5))

df['Date'] = pd.to_datetime(df['Date'])
df_2021 = df[df['Date'] >= '2021']
 
max_price = df_2021['Close'].max()
min_price = df_2021['Close'].min()

print('최고 종가: ', max_price)
print('최저 종가: ', min_price)