import csv
students=[]
while True:
    print("1 add")
    print("2 view")
    print("3 search")
    print("4 delet")
    print("5 avg")
    print("6 save")
    print("7 load")
    print("8 exit")


    choice=input("enter your choice")
#add
    if choice=="1":
        name=input("enter name:")
        try:
            marks=int(input("enter marks:"))
            students.append({"name":name,"marks":marks})
            print("student added succesfully!")
        except:
            print("invalid marks")
#view

    elif choice=="2":
        if not students:
            print("not student found")
        else:
            for s in students:
                print(s["name"],"-",s["marks"])
#search 

    elif choice=="3":   
        name= input("enter name to search") 
        found=False
        for s in students:
            if s["name"]==name:
                print("found:", s["name"],s["marks"])
                found=True
        if not found:
            print("Not found") 

#Deleted

    elif choice=="4":
        name=input("delet name:")
        new_list=[]

        for s in students:
            if s["name"] != name:
                new_list.append(s)
        students=new_list
        print("deleted") 

#avg

    elif choice=="5":
        if len(students)==0:
            print("no data") 
        else:
            total=0
            for s in students:
                total += s["marks"]  
            print("avg:", total/len(students)) 

    # SAVE
    elif choice == "6":
        with open("data.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for s in students:
                writer.writerow([s["name"], s["marks"]])
        print("Saved!")

    # LOAD
    elif choice == "7":
        try:
            with open("data.csv", "r") as f:
                reader = csv.reader(f)
                students = []
                for row in reader:
                    students.append({"name": row[0], "marks": int(row[1])})
            print("Loaded!")
        except:
            print("No file found")

    # EXIT
    elif choice == "8":
        break

    else:
        print("Invalid choice")

    



    
