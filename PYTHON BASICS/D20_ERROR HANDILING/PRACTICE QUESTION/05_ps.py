n=int(input("enter a valid no:"))
table=[n*i for i in range (1,11)]
with open("PRACTICE QUESTION/table.txt","a") as f:
    f.write( f"table of {n} table is {str(table)}\n")