class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums: List[int]) -> int:
        two_prev, prev = 0, 0

        for num in nums:
            max_rob = max(num + two_prev, prev)
            two_prev = prev
            prev = max_rob

        return max_rob
