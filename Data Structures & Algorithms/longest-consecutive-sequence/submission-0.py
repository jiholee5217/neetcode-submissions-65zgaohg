class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0;

        for n in nums:
            if n - 1 not in num_set:
                length = 0
                while n + length in num_set:
                    length += 1
                max_seq = max(length, max_seq)

        return max_seq
