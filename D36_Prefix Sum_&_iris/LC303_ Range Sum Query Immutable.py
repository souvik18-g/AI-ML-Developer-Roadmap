class NumArray:

    def __init__(self, nums):

        # self.prefix = [0]

        # create list:
        # [0]

        self.prefix=[0]

        for i in nums:

            # FIRST LOOP
            # i = 2
            # self.prefix[-1] = 0
            # 0 + 2 = 2
            # append 2
            # [0,2]

            # SECOND LOOP
            # i = 4
            # self.prefix[-1] = 2
            # 2 + 4 = 6
            # append 6
            # [0,2,6]

            # THIRD LOOP
            # i = 3
            # self.prefix[-1] = 6
            # 6 + 3 = 9
            # append 9
            # [0,2,6,9]

            # FOURTH LOOP
            # i = 6
            # self.prefix[-1] = 9
            # 9 + 6 = 15
            # append 15
            # [0,2,6,9,15]

            # FIFTH LOOP
            # i = 8
            # self.prefix[-1] = 15
            # 15 + 8 = 23
            # append 23
            # [0,2,6,9,15,23]

            self.prefix.append(self.prefix[-1]+i)


    def sumRange(self, left: int, right: int) -> int:

        # left = 1
        # right = 3

        # self.prefix[right+1]
        # self.prefix[4]
        # = 15

        # self.prefix[left]
        # self.prefix[1]
        # = 2

        # 15 - 2 = 13

        return self.prefix[right+1]-self.prefix[left]