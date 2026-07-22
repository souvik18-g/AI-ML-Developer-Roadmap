import pandas as pd

df= pd.read_csv("Pandas practice 1.csv")

print(df.head(10))  # Display the first 10 rows of the DataFrame
print(df.tail(10))  # Display the last 10 rows of the DataFrame

print(df.head())  # as a default, this will display the first 5 rows of the DataFrame
print(df.tail()) # as a default, this will display the last 5 rows of the DataFrame