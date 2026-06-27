class Solution:
# class → creates a class
# Solution → class name required by LeetCode

    def diameterOfBinaryTree(self, root):
    # def → define a function
    # diameterOfBinaryTree → function name
    # self → current Solution object
    # root → root node of tree

        self.diameter = 0
        # self.diameter → variable stored in Solution object
        # = → assignment operator
        # 0 → initial diameter before calculation

        def height(node):
        # def → define helper function
        # height → function name
        # node → current tree node being processed

            if node is None:
            # if → condition
            # node → current node
            # is → identity operator
            # None → no node exists

                return 0
                # return → send value back
                # 0 → height of empty tree

            left = height(node.left)
            # left → variable
            # = → assignment
            # height() → recursive function call
            # node.left → left child
            #
            # Meaning:
            # Find height of left subtree

            right = height(node.right)
            # right → variable
            # = → assignment
            # height() → recursive function call
            # node.right → right child
            #
            # Meaning:
            # Find height of right subtree

            self.diameter = max(
                self.diameter,
                left + right
            )
            # self.diameter → current best diameter
            # max() → chooses bigger value
            # left + right → diameter through current node
            #
            # Meaning:
            # compare old diameter
            # with current node's diameter
            # keep larger one

            return 1 + max(left, right)
            # return → send height back
            # 1 → current node itself
            # max() → choose taller subtree
            #
            # Meaning:
            # current node
            # + tallest subtree height

        height(root)
        # start recursion from root

        return self.diameter
        # return final largest diameter found