import pandas as pd

df=pd.read_csv("output.csv")
print(df.info()) # its used to get a concise summary of the DataFrame, including the number of non-null entries, data types, and memory usage.