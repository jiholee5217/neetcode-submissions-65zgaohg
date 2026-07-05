class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # we are going to use this for fast look ups to see if the 
                     # complement of target - nums[i] exist

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i


