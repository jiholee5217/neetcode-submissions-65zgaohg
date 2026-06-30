class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashmap:
                return [hashmap[value], i]
            else:
                hashmap[nums[i]] = i

