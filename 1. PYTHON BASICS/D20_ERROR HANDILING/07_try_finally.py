# try:
#     a=int(input("enter a valid no: "))
#     print(a)
# except Exception as b:
#     print(b)
# finally:
#     print("its else section")   


def main():

    try:

        a=int(input("enter a valid no: "))
        print(a)
    except Exception as b:

        print(b)
    finally:               #if we make a function then finally have a important role because then without finally value not return but othrtwise like 1st part their finally is alwayes return like print  

        print("its else section")   
main()     