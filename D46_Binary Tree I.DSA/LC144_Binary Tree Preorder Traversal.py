# class = blueprint/template
# Solution = class name required by LeetCode

class Solution:


    # def = function definition
    # preorderTraversal = function name
    # self = current object of class
    # root = starting node of binary tree

    def preorderTraversal(self, root):


        # res = empty list
        # stores final preorder answer

        res = []


        # helper recursive function

        def preorder(root):


            # if root exists
            # means node is not None

            if root:


                # append = add value into list
                # root.val = current node value

                res.append(root.val)


                # recursive call on left subtree

                preorder(root.left)


                # recursive call on right subtree

                preorder(root.right)



        # start recursion from root node

        preorder(root)


        # return final preorder list

        return res