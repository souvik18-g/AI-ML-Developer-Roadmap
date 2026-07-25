rows =int(input("enter value:"))

for i in range(rows):

    # Print spaces
    for j in range( i ):
                print(" ", end="")
    # Print stars
    for k in range(2 *(rows-i)- 1):
        print("*", end="")
    
    
    print()