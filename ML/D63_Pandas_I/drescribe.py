import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    'Age': [25, 30, 35, 40, 28, 32, 29, 31, 27, 33],
    'performace_score': [85, 90, 78, 92, 88, 95, 80, 87, 91, 89],
    'Salary': [70000, 80000, 90000, 100000, 75000, 85000, 95000, 105000, 72000, 88000]
}

df = pd.DataFrame(data)
print(df.describe())