

"""
=========================================
DAY 55 - KAGGLE LEARN PYTHON II
=========================================

Topics Covered:
1. Strings
2. Dictionaries
3. Working with External Libraries

What I Learned:
- String methods
- Dictionary operations
- Importing Python libraries
- Using external modules

Platform:
https://www.kaggle.com/learn/python

Status:
Completed all remaining modules and exercises.
Downloaded Kaggle Python Certificate.
Added certificate to LinkedIn.
"""

print("Day 55 - Kaggle Python completed.")

# Strings
name = "Souvik"

print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("S", "A"))

# Dictionary
student = {
    "name": "Souvik",
    "age": 19,
    "course": "B.Tech"
}

print(student)
print(student["name"])

# External Libraries
import math
import random

print(math.sqrt(81))
print(random.randint(1, 10))