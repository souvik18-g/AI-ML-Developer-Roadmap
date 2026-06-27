# =====================================================
#                 NODE CLASS
# =====================================================


# class = blueprint/template for creating objects
class Node:

    # __init__ = constructor
    # runs automatically when object is created

    # self = current object itself
    # data = value passed by user

    def __init__(self, data):

        # store value inside node
        self.data = data

        # left child initially empty
        self.left = None

        # right child initially empty
        self.right = None



# =====================================================
#              CREATE ROOT NODE
# =====================================================


# create node with value 1
# root variable stores first node of tree

root = Node(1)


# Tree currently:
#
#       1
#      / \
#   None None



# =====================================================
#              CREATE LEFT CHILD
# =====================================================


# attach node 2 to left side of root

root.left = Node(2)


# Tree now:
#
#       1
#      /
#     2



# =====================================================
#              CREATE RIGHT CHILD
# =====================================================


# attach node 3 to right side of root

root.right = Node(3)


# Tree now:
#
#       1
#      / \
#     2   3



# =====================================================
#              CREATE MORE NODES
# =====================================================


# attach node 4 to left of node 2

root.left.left = Node(4)


# attach node 5 to right of node 2

root.left.right = Node(5)



# Final Tree:
#
#           1
#          / \
#         2   3
#        / \
#       4   5



# =====================================================
#              PREORDER TRAVERSAL
# =====================================================


# preorder order:
#
# Root -> Left -> Right
#
# Expected output:
# 1 2 4 5 3


def preorder(root):

    # base case
    # if node does not exist stop recursion

    if root is None:
        return


    # print current node value

    print(root.data, end=" ")


    # go left side

    preorder(root.left)


    # go right side

    preorder(root.right)



# =====================================================
#              INORDER TRAVERSAL
# =====================================================


# inorder order:
#
# Left -> Root -> Right
#
# Expected output:
# 4 2 5 1 3


def inorder(root):

    # stop if node absent

    if root is None:
        return


    # go left first

    inorder(root.left)


    # print current node

    print(root.data, end=" ")


    # go right

    inorder(root.right)



# =====================================================
#              POSTORDER TRAVERSAL
# =====================================================


# postorder order:
#
# Left -> Right -> Root
#
# Expected output:
# 4 5 2 3 1


def postorder(root):

    # stop recursion if node absent

    if root is None:
        return


    # left subtree

    postorder(root.left)


    # right subtree

    postorder(root.right)


    # print current node at end

    print(root.data, end=" ")



# =====================================================
#              BFS / LEVEL ORDER
# =====================================================


# BFS = Breadth First Search
#
# Goes level by level
#
# Uses Queue
#
# Expected output:
# 1 2 3 4 5


# import deque for queue operations

from collections import deque


def level_order(root):

    # if tree empty stop

    if root is None:
        return


    # create queue
    # initially store root node

    q = deque([root])


    # loop runs until queue becomes empty

    while q:


        # remove first element from queue

        node = q.popleft()


        # print node value

        print(node.data, end=" ")


        # if left child exists
        # add into queue

        if node.left:
            q.append(node.left)


        # if right child exists
        # add into queue

        if node.right:
            q.append(node.right)



# =====================================================
#              FUNCTION CALLS
# =====================================================


print("Preorder Traversal:")
preorder(root)

print("\n")


print("Inorder Traversal:")
inorder(root)

print("\n")


print("Postorder Traversal:")
postorder(root)

print("\n")


print("Level Order BFS Traversal:")
level_order(root)