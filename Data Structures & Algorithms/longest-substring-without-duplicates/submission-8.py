class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            cur_len = right - left + 1
            longest = max(longest, cur_len)

        return longest

     


    # z x y z x y z
    # l
    #       r    
            
    # seen = {z, x, y, }
