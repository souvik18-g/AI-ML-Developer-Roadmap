import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    'Age': [25, 30, 35, 40, 28, 32, 29, 31, 27, 33],
    'performace_score': [85, 90, 78, 92, 88, 95, 80, 87, 91, 89],
    'Salary': [70000, 80000, 90000, 100000, 75000, 85000, 95000, 105000, 72000, 88000]
}

df = pd.DataFrame(data)
print(df) # Display the DataFrame

high_salary =df[df['Salary'] > 90000] # Filter rows where Salary is greater than 90000
print(high_salary) # Display the filtered DataFrame

# Filter rows where Age is greater than 30 & Salary is greater than 80000
print("Filter rows where Age is greater than 30 & Salary is greater than 80000")
filtered_data_and = df[(df['Age'] > 30) & (df['Salary'] > 80000)] # use here & condition
print(filtered_data_and) # Display the filtered DataFrame

print("Filter rows where Age is greater than 35 or Salary is greater than 90000 or performance_score is greater than 90")
filtered_data_or = df[(df['Age'] > 35) | (df['Salary'] > 90000) | (df['performace_score'] > 90)] # use here | condition(or condition)
print(filtered_data_or) # Display the filtered DataFrame

