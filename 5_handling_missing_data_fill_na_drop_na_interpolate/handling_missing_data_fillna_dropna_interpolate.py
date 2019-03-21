import pandas as pd
df = pd.read_csv("weather_data.csv")#It will csv file and fill blank value to NaN.
print(df)

df.set_index('day',inplace=True)#'Day' will work like an index
print(df)

new_df = df.fillna(0)#Fill all field with value NaN with 0(Strign col) and 0.0(integer col)
print(new_df)

#--------------------------------------------
##Fill Custom value to column
new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'No Event'
    })
print(new_df)
#--------------------------------------------

#--------------------------------------------
##Fill Upper col  value to NaN column
new_df = df.fillna(method="ffill")
print(new_df)
#--------------------------------------------

##Fill Down col value to Upper NaN column
new_df = df.fillna(method="bfill")
print(new_df)

##Fill Down col value to Upper NaN column in all row value
new_df = df.fillna(method="bfill", axis="columns") # axis is either "index" or "columns"
print(new_df)

new_df = df.interpolate()
print(new_df)

#It will show only that row which don't have any NaN value
new_df = df.dropna()
print(new_df)

new_df = df.dropna(thresh=1)
print(new_df)