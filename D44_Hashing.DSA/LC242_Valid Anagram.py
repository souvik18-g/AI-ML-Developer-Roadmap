class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # anagrams must have same length
        # example:
        # "rat" and "car"
        # both length 3
        #
        # but:
        # "rat" and "rats"
        # lengths different
        # impossible to be anagram
        if len(s) != len(t):
            return False

        # create empty hashmap(dictionary)
        #
        # this stores:
        # character -> frequency count
        #
        # example:
        # {
        #   'a':2,
        #   'b':1
        # }
        count = {}

        # loop through every character in string s
        #
        # example:
        # s = "anagram"
        #
        # loop values:
        # a n a g r a m
        for ch in s:

            # count.get(ch,0)
            #
            # means:
            # find key ch in dictionary
            # if not found return 0
            #
            # then +1 increases frequency
            #
            # example:
            # first 'a'
            # 0 + 1 = 1
            #
            # second 'a'
            # 1 + 1 = 2
            count[ch] = count.get(ch, 0) + 1

        # after first loop
        #
        # if s = "anagram"
        #
        # dictionary becomes:
        #
        # {
        #   'a':3,
        #   'n':1,
        #   'g':1,
        #   'r':1,
        #   'm':1
        # }

        # now loop through second string
        #
        # example:
        # t = "nagaram"
        #
        # loop:
        # n a g a r a m
        for ch in t:

            # if character not present in dictionary
            # then not an anagram
            #
            # example:
            # s = "abc"
            # t = "abd"
            #
            # 'd' not found
            #
            # immediately return False
            if ch not in count:
                return False

            # decrease frequency
            #
            # because this character matched once
            #
            # example:
            #
            # before:
            # 'a':3
            #
            # after:
            # 'a':2
            count[ch] -= 1

            # if frequency becomes negative
            # means extra character exists in t
            #
            # example:
            #
            # s = "aab"
            # t = "aaa"
            #
            # after third 'a':
            #
            # 'a': -1
            #
            # invalid
            if count[ch] < 0:
                return False

        # if all checks passed
        # both strings are anagrams
        return True