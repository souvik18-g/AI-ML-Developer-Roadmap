# try:
#     a=int(input("hey,enter a valiid no:"))
#     print(a)

# except Exception as b:
#     print(b)  
# print("thank you")      

try:
    a=int(input("hey,enter a valiid no:"))
    print(a)
except ValueError as v:
    print("hey")
    print(v)
except Exception as b:
    print(b)  


