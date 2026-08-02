import csv


with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    students = [
    ["Souvik", 19, 95],
    ["Rahul", 20, 88],
    ["Ankit", 21, 90]
]

    writer.writerows(students)

    
    