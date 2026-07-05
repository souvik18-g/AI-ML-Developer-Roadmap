class Solution:                   # Create a class named Solution

    def searchBST(self, root, val):  # Function to search val in BST
        
        if root is None:             # If current node doesn't exist
            return None              # Value not found, return None

        elif val == root.val:        # If target value equals current node value
            return root              # Return this node (found)

        elif val < root.val:         # If target is smaller than current node
            
            return self.searchBST( root.left,val)  # Call same function again (recursion)   # Move to left child
                                                    # Search same target value
            

        else:                        # Means val > root.val
            
            return self.searchBST( root.right,val)  # Call same function again
                              # Move to right child
                                 # Search same target value
            