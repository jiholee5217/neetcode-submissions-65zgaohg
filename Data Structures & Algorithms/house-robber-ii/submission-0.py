class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))


    def rob_helper(self, nums):
        previous_house = 0
        two_houses_ago = 0

        for num in nums:
            best = max(num + two_houses_ago, previous_house)
            previous_house, two_houses_ago = best, previous_house

        return max(previous_house, two_houses_ago)