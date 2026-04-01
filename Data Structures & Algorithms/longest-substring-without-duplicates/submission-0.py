class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest_len = 0
        charSet = set()
        
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            longest_len = max(right - left + 1, longest_len)
            right += 1
        return longest_len


            # while s[right] not in charSet:
            #     right += 1
            #     charSet.add[s[right]]
            # if s[right] in charSet:
            #     left += 1