class Solution:
    def guessNumber(self, n: int) -> int:

        # starting range
        low = 1
        high = n

        # continue until search space valid
        while low <= high:

            # find middle number
            mid = (low + high) // 2

            # ask LeetCode API:
            # is my guessed number correct?
            result = guess(mid)

            # if API returns 0
            # mid is correct answer
            if result == 0:
                return mid

            # if API returns 1
            # my guess is TOO LOW
            # hidden number is bigger
            elif result == 1:

                # remove left half INCLUDING mid
                low = mid + 1

            # else API returned -1
            # my guess is TOO HIGH
            else:

                # remove right half INCLUDING mid
                high = mid - 1