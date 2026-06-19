class Solution:
    def maxSubarraySum(self, arr, k):
        
        window_sum = sum(arr[:k]) # here the sum of till Kth value
        max_sum = window_sum # here store it 

        for i in range(k, len(arr)): # start from k value to total length
            window_sum = window_sum + arr[i] - arr[i-k] #store it in after check previus total valus are big so not here sequence wise add & remove previous values 
                                                         #new sum=old sum+ new entering value- old leaving value
            max_sum = max(max_sum, window_sum) # compare max values 

        return max_sum