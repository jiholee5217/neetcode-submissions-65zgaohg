class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        indices = []
        for i in range(len(nums)):
            hMap[nums[i]] = i # this add int as key and index as value to hMap

        for i in range(len(nums)):
            if (target - nums[i] in hMap and i != hMap[target - nums[i]]):
                indices = [i, hMap[target - nums[i]]]
                return indices
            else:
                continue