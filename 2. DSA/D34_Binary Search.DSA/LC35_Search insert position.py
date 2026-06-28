class Solution:
    def searchInsert(self, nums, target: int) -> int: #in question there a list which is sorted 
        # in list we take first index & last index
        low=0
        high=len(nums)-1
         #start while loop , when low <= high
        while low<=high:
            # make a mid index 
            mid=(low+high)//2
            # if mid index value equals to our target value then retun the mid value so we found target also
            if nums[mid]==target:
                return mid
            # when 1st step not satisfied then we run elif part where mid index value lesser than target we increas the value
            elif nums[mid]<target:
                low=mid+1
                 #when previous steps not satisfied then we run else part where mid index value greater than target we reduce the value
            else:
                high=mid-1

        #when we not found our targeted value then that will be add in sortlly in list        
        return low
