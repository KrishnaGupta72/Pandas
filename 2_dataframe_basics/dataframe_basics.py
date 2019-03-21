import pandas as pd
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
print(df)#Create dataframes in tabular format like Excel file

# Reading data from an Excel File
df = pd.read_csv("weather_data.csv")
print(df)#Prining dataframes in tabular format like Excel
print(df.shape) #
#(6,4)
rows, columns = df.shape
print("Rows: {} & Column: {}".format(rows,columns))#
print(df.head(2)) #Print only first 2 records with Headers
print(df.tail(2)) #Print only last 2 records with Headers
print(df[1:3])#Print records with Headers from 1 to 2 index
print(df.columns)#Index(['day', 'temperature', 'windspeed', 'event'], dtype='object')
print(df['day'])#or  print(df.day) #It will print all day column records without Field name.
print(df[['day','event']])#It will print only day to event column
print(df['temperature'].max())#35
print(df['event'][df['temperature']==df['temperature'].max()])#Sunny
print(df[df['temperature'] == df['temperature'].max()])#Like SQL in PANDAS () select * from where
print(df['temperature'].std())#3.8297084310253524
print(df['event'].max())#Sunny # But mean() won't work since data type is string
print(df.describe()) #Do calculation(count/mean/std/min/25%/50%/75%/max) over integer valued column
print(df.set_index('day'))
df.set_index('day', inplace=True)
print(df)
print(df.index)
print(df.loc['1/2/2017'])

df.reset_index(inplace=True)
print(df.head())

df.set_index('event',inplace=True) # this is kind of building a hash map using event as a key
print(df)

df.loc['Snow']
print(df)