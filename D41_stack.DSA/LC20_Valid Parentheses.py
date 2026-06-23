class Solution:
    def isValid(self, s: str) -> bool:

        # stack for storing opening brackets
        stack = []

        # mapping closing -> opening
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        # traverse each character
        for char in s:

            # if opening bracket
            if char in mapping.values():

                # push into stack
                stack.append(char)

            # if closing bracket
            else:

                # stack empty OR mismatch
                if not stack or stack[-1] != mapping[char]:
                    return False

                # matched bracket -> remove top here evry tiime check that last prerenthese are matched or not if matched then its pop(remove) & its contineo
                stack.pop()
        # then checked all & poped this process removed all parentheses 
        # valid only if stack empty
        return len(stack) == 0
    
    