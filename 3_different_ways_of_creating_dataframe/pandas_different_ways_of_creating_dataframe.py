import pandas as pd
#Read from a CSV file
df = pd.read_csv("weather_data_1.csv")
print(df)

#Read from an Excel file
df=pd.read_excel("weather_data_1.xlsx","Sheet1")
print(df)

#Creating a dataframe in JSON format
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
print(df)

#Creating a dataframe in List of Tuple format
weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
print(df)


#Creating a dataframe in List of Tuple format
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},

]
df = pd.DataFrame(data=weather_data, columns=['day', 'temperature', 'windspeed', 'event'])
print(df)