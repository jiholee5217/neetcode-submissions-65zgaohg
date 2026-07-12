class Solution:
    def findMin(self, nums: List[int]) -> int:
        # set left index 0 and set right to the last index of the array nums
        left, right = 0, len(nums) - 1 

        # loop while left is less than right
        while left < right:
            # mid is equal to the integer floor of (left + right) divided by 2
            mid = (left + right) // 2
            # if nums at mid is greater than nums at right
            if nums[mid] > nums[right]:
                # set the left index to mid + 1
                left = mid + 1
            # else
            else:
                # set the right index to mid 
                right = mid
        # return nums[left] or nums[right] both should be the minimum
        return nums[right]