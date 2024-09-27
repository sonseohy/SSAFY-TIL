import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = 'archive/NFLX.csv'
df = pd.read_csv(csv_path, usecols=range(0, 5))
print(df)