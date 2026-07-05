"""
=========================================
DAY 54 - KAGGLE LEARN PYTHON I
=========================================

Topics Covered:
1. Hello Python
2. Functions
3. Booleans and Conditionals
4. Lists
5. Loops and List Comprehensions

What I Learned:
- Writing Python programs
- Creating and calling functions
- Using if, elif and else
- Working with lists
- Using for and while loops
- Creating list comprehensions

Platform:
https://www.kaggle.com/learn/python

Status:
Completed all 5 modules and exercises.
"""

print("Day 54 - Kaggle Python completed.")

# Function
def square(x):
    return x * x

print(square(5))

# Boolean
age = 19

if age >= 18:
    print("Adult")
else:
    print("Minor")

# List
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

# List Comprehension
squares = [x*x for x in numbers]
print(squares)