import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False) # Save the DataFrame to a CSV file without the index

df.to_excel("output.xlsx", index=False) # Save the DataFrame to an Excel file without the index

df.to_json("output.json", orient="records") # Save the DataFrame to a JSON file with records orientation