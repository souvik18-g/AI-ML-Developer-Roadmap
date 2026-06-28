class Solution:
# class → creates a class
# Solution → class name required by LeetCode

    def maxDepth(self, root):
    # def → define a function
    # maxDepth → function name
    # self → current Solution object
    # root → root node of the tree

        if root is None:
        # if → condition check
        # root → current node
        # is → identity operator
        # None → means no node / empty tree

            return 0
            # return → send value back
            # 0 → depth of empty tree is 0

        left = self.maxDepth(root.left)
        # left → variable name
        # = → assignment
        # self → current Solution object
        # . → access member
        # maxDepth() → recursive function call
        # root.left → left child of current node
        #
        # Meaning:
        # "Find depth of left subtree and store in left"

        right = self.maxDepth(root.right)
        # right → variable name
        # = → assignment
        # self.maxDepth() → recursive call
        # root.right → right child
        #
        # Meaning:
        # "Find depth of right subtree and store in right"

        return 1 + max(left, right)
        # return → send answer back
        # 1 → current node itself
        # + → add
        # max() → choose larger value
        # left → left subtree depth
        # right → right subtree depth
        #
        # Meaning:
        # current node
        # + deepest subtree