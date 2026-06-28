class Solution:
    def climbStairs(self, n: int) -> int:

        # Base DP values
        one = 1      # Ways to reach current stair 
        two = 1      # Ways to reach previous stair  

        # Run n-1 times because one and two are already initialized
        for i in range(n - 1):

            # Save current value of one
            temp = one

            # Calculate next Fibonacci/DP value
            one = one + two

            # Move old one to two
            two = temp

        # Final answer
        return one
    
    