class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sublist = {}
        for str in strs:
            frequency = [0] * 26

            for char in str:
                frequency[ord(char) - ord('a')] += 1

            if tuple(frequency) not in sublist:
                sublist[tuple(frequency)] = []
            sublist[tuple(frequency)].append(str)

        return list(sublist.values())
        


# ord("char") - ord("a") 91 91 = 1
# 0 to 25 will represent a to z
# convert an array index from 0 to 25 that stores the frequency of that letter showing up
# {tuple of integers : list of anagrams}