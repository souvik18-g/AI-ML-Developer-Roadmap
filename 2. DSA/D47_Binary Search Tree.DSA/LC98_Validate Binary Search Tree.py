class Solution:                    # LeetCode class

    def isValidBST(self, root):    # Function to check BST

        self.prev = float('-inf')  # Previous value starts at -infinity

        def inorder(node):         # Helper function for inorder traversal

            if node is None:       # If no node exists
                return True        # Empty tree is valid

            if not inorder(node.left):  # First visit left subtree
                return False           # If left subtree invalid

            if node.val <= self.prev:  # Current value must be greater
                return False           # Not sorted -> Not BST

            self.prev = node.val       # Save current value as previous

            return inorder(node.right) # Visit right subtree

        return inorder(root)      # Start traversal from root