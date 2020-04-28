import pandas as pd
import re

df = pd.read_csv('comments_6.csv', encoding='utf-16')
print(df.isnull().sum())
print(df.dropna())