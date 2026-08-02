def Reverse_String(s):
    if s == "":
        return s
    else:
        return Reverse_String(s[1:]) + s[0]

s = input("Enter a string: ")
result = Reverse_String(s)  
print(f"The reverse of the string '{s}' is '{result}'.")


# def Reverse_String(s):
#     if len(s) == 0:
#         return s
#     else:
#         return s[-1] + Reverse_String(s[:-1])
# s = input("Enter a string: ")
# result = Reverse_String(s)  
# print(f"The reverse of the string '{s}' is '{result}'.")