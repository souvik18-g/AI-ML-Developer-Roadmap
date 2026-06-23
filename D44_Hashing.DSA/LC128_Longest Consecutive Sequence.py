class Solution:
    def longestConsecutive(self, nums):

        # convert list into set
        #
        # WHY?
        # because searching in set is very fast O(1)
        #
        # example:
        # nums = [100,4,200,1,3,2]
        #
        # set becomes:
        # {100,4,200,1,3,2}
        #
        # duplicates also removed automatically
        s = set(nums)

        # store longest sequence length found
        #
        # initially no sequence found
        # so start with 0
        #
        # NOT index
        # this stores answer
        longest = 0

        # loop through every number in set
        #
        # example loop:
        # 100
        # 4
        # 200
        # 1
        # 3
        # 2
        #
        # order may change because set unordered
        for num in s:

            # check if current number is START of sequence
            #
            # IMPORTANT LOGIC OF ENTIRE PROBLEM
            #
            # example:
            # num = 4
            #
            # check:
            # 4-1 = 3
            #
            # if 3 exists in set
            # then 4 is NOT start
            #
            # sequence already started from smaller number
            #
            # only start counting from first number
            #
            # example:
            # sequence:
            # 1,2,3,4
            #
            # only 1 starts counting
            #
            # 2,3,4 skipped
            #
            # this avoids repeated work
            if num - 1 not in s:

                # current sequence length
                #
                # initially current number itself
                #
                # example:
                # num = 1
                #
                # sequence:
                # 1
                #
                # length = 1
                length = 1

                # expand sequence forward
                #
                # example:
                # num = 1
                #
                # check:
                # 1+1 = 2
                #
                # if 2 exists:
                # length becomes 2
                #
                # then:
                # 1+2 = 3
                #
                # if 3 exists:
                # length becomes 3
                #
                # continue until number missing
                while num + length in s:

                    # increase sequence length
                    #
                    # example:
                    # sequence:
                    # 1,2,3,4
                    #
                    # length changes:
                    # 1 -> 2 -> 3 -> 4
                    length += 1

                # compare current sequence length
                # with longest sequence found so far
                #
                # example:
                # current longest = 1
                # current length = 4
                #
                # max(1,4) = 4
                #
                # update answer
                longest = max(longest, length)

        # return final longest sequence length
        #
        # example:
        # nums = [100,4,200,1,3,2]
        #
        # sequence:
        # 1,2,3,4
        #
        # answer:
        # 4
        return longest