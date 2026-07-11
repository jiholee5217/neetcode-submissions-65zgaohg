class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        char_max = [0] * 26
        max_len = 0
        cur_len = 0

        while right < len(s): 
            char_max[ord(s[right]) - ord('A')] += 1 # increase index of that char by 1 
            while (right - left + 1) - max(char_max) > k:
                char_max[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
