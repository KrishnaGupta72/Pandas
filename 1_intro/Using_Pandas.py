##By using PANDAS working with CSV files.
import pandas as pd
df = pd.read_csv('nyc_weather.csv')
print(df)
print(df['Temperature'].max())
print(df['EST'][df['Events']=='Rain'])#Must write from the starting Field names
print(df.fillna(0, inplace=True))
print(df['WindSpeedMPH'].mean())