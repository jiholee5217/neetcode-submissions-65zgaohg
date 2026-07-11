class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        right = 0
        freq = [0] * 26
        longest = 0 

        while right < len(s):
            freq[ord(s[right]) - ord('A')] += 1
            while (right - left + 1) - max(freq) > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1
            longest = max(longest, right - left + 1)
            right += 1

        return longest
        