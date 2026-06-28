print("souvik")  #due to this run 1 step its O(1)
num=[1,2,3,4,5]
print(num[2])

# for i in num:  #due to its runs 5 times evey time like 1at first again 2 so on thats why its O(n) not O(1) ,O(1) needs to just 1 step buthere 5 time runs 
#     print(i)

for i in range(400):   # so here range fixed not n times so here not run n times its O(1)
    print(i)   
    # test commit