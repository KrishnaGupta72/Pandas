import pandas as pd
df = pd.read_csv("stock_data.csv")
print(df)

df = pd.read_csv("stock_data.csv", skiprows=1)#Will  skip first row that is Header row
print(df)

df = pd.read_csv("stock_data.csv", header=1) # skiprows and header are kind of same
print(df)

df = pd.read_csv("stock_data.csv",  nrows=2)#show 3 rows with Headers.
print(df)

df = pd.read_csv("stock_data.csv", na_values=["n.a.", "not available",-1])#Will replace all ""n.a.", "not available",-1" entry with NaN
print(df)

#''''''''''''''''''''''''''''''''''''
df = pd.read_csv("stock_data.csv",  na_values={
        'eps': ['not available'],
        'revenue': [-1],
        'people': ['not available','n.a.']
    })
print(df)#It will replace by particular column wise entry.

#Write data from stock_data.csv file into new.csv
df.to_csv("new.csv", index=False)
print(df.columns)#Gives a list of all columns name

df.to_csv("new.csv",header=False)#
print(df)
#''''''''''''''''''''''''''''''''''''

#''''''''''''''''''''''''''''''''''''
#To replace particular column data by using PANDAS from stock_data.xlsx file
def convert_people_cell(cell):
    if cell == "n.a.":
        return 'Sam Walton'
    return cell

def convert_price_cell(cell):
    if cell == "n.a.":
        return 50
    return cell

df = pd.read_excel("stock_data.xlsx", "Sheet1", converters={
    'people': convert_people_cell,
    'price': convert_price_cell
})
print(df)
#''''''''''''''''''''''''''''''''''''


## Write two dataframes to two separate sheets in excel

df_stocks = pd.DataFrame({
    'tickers': ['GOOGL', 'WMT', 'MSFT'],
    'price': [845, 65, 64 ],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather =  pd.DataFrame({
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'event': ['Rain', 'Sunny', 'Snow']
})

with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name="stocks")
    df_weather.to_excel(writer, sheet_name="weather")