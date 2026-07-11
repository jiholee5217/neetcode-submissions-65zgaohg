class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exist = set()
        left = 0
        right = 0
        longest = 0

        while right < len(s):
            while s[right] in exist:
                exist.remove(s[left])
                left += 1
            exist.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1

        return longest
            
