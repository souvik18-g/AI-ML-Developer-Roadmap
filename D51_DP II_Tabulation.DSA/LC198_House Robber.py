class Solution:
    def rob(self, nums) -> int:

        rob1, rob2 = 0, 0   # Previous two DP values which 0,0 because no value previously saved

        for n in nums:      # Current house money

            temp = max(n + rob1, rob2)  # Rob or skip here we find max value with one gap 

            rob1 = rob2     # Shift previous value

            rob2 = temp     # Store current maximum

        return rob2         # Final answer