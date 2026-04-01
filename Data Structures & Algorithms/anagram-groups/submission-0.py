class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping tuples of character count to list of strings

        for s in strs:
            count = [0] * 26 # create an array of size 26 filled with all zeroes
            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return list(result.values())