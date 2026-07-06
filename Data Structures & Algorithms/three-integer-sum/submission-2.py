class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                if nums[left] + nums[right] + nums[i] == 0:
                    result.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1

        return result