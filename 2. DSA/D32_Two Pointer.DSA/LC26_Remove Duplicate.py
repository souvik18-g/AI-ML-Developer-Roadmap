class Solution:
    def removeDuplicates(self,nums) -> int:
        i = 0    # indexing start with 0 

        for j in range(1, len(nums)): # loop start from 1 to len of nums
            if nums[j] != nums[i]:  # if j's index values not equal to i's index value
                i += 1 # increase 1 evry time
                nums[i] = nums[j]  # change value 

        return i + 1   # array needs total lenght but i start from o due to indexing so convert length so do it
    
    


