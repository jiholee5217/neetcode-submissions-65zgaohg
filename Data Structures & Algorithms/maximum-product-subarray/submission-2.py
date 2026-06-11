class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1
        
        for num in nums:
            tempCurMax = curMax * num
            curMax = max(num, num * curMax, num * curMin)
            curMin = min(tempCurMax, num * curMin, num)
            res = max(res, curMax, curMin)
        return res 