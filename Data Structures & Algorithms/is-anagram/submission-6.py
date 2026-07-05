class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = {}
        tCount = {}

        for i in range(len(s)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1

        if sCount == tCount:
            return True
        return False

# if string s and string t length is not equal return False
# otherwise create a hashmap for s and t and loop through both strings and for the
# for each character we encounter at i index, we add that character to the hashmap
# 