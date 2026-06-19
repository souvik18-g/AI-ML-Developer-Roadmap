num=[1,2,3]
num.insert(1,12) #its O(n) bcz here at 1st in index 1 came 12 then next elements are index place shifted so its O(n)
print(num)

num=[1,2,3]
num.insert(3,12) #It is O(1) because inserting at the end does not require shifting elements, so the number of operations does not depend on n.
print(num)