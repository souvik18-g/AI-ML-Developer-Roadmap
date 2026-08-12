# try:
#     a=int(input("hey,enter a valiid no:"))
#     print(a)

# except Exception as b:
#     print(b)  
# print("thank you")      

try:
    a=int(input("hey,enter a valiid no:"))
    print(a)                                    # # Print the number if conversion succeeds
except ValueError as v:                           ## Catch only ValueError
    print("hey")                                  # # Print "hey" when ValueError occurs
    print(v)                                           #  # Print the ValueError message
except Exception as b:                              #  #Catch any other type of exception
    print(b)                                       # # Print the exception message


