from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        # create hashmap(dictionary)
        # defaultdict(list) means:
        # if key not present, automatically create empty list []
        groups = defaultdict(list)

        # loop through every word in list
        for word in strs:

            # sorted(word)
            # converts word into sorted character list
            #
            # example:
            # "eat" -> ['a','e','t']
            # "tea" -> ['a','e','t']
            #
            # ''.join() converts list back into string
            #
            # ['a','e','t'] -> "aet"
            #
            # this sorted string becomes key
            # all anagrams produce same key
            key = ''.join(sorted(word))

            # append current word into that key group
            #
            # example:
            # groups["aet"].append("eat")
            # groups["aet"].append("tea")
            #
            # result:
            # {
            #   "aet":["eat","tea"]
            # }
            groups[key].append(word)

        # groups.values() gives all grouped lists
        #
        # example:
        # dict_values([
        #   ["eat","tea","ate"],
        #   ["tan","nat"],
        #   ["bat"]
        # ])
        #
        # convert into normal list
        return list(groups.values())