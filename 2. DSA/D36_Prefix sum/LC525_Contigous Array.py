class Solution:

    def findMaxLength(self, nums):

        # stores running sum
        prefix_sum = 0

        # stores longest valid subarray length
        max_len = 0

        # hashmap stores:
        # prefix_sum : first index where it appeared
        #
        # 0:-1 means:
        # before array starts,
        # prefix sum 0 already exists
        hashmap = {0: -1}

        # loop through array
        for i in range(len(nums)):

            # convert 0 -> -1
            if nums[i] == 0:
                prefix_sum -= 1

            # convert 1 -> +1
            else:
                prefix_sum += 1

            # if same prefix sum seen before,
            # then middle subarray sum = 0
            # means equal 0s and 1s
            if prefix_sum in hashmap:

                # calculate subarray length
                length = i - hashmap[prefix_sum]

                # update maximum length
                max_len = max(max_len, length)

            # store first occurrence only
            else:
                hashmap[prefix_sum] = i

        # return longest valid length
        return max_len