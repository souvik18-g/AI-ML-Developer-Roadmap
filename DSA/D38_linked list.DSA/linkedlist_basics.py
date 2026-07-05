class Node:
    def __init__(self,data):
        self.data=data
        self.next=None




#creats nodes 
        
head=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)

#connect nodes

head.next=second
second.next=third
third.next=fourth

#traversal

curr=head  #curr starts from first node

while curr:
    print(curr.data)
    curr=curr.next