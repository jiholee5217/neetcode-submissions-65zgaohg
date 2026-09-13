class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # maps values to indices
        for i in range(len(nums)):
            hashMap[nums[i]] = i

        for j in range(len(nums)):
            complement = target - nums[j]
            if complement in hashMap and j != hashMap[complement]:
                return [j, hashMap[complement]]
