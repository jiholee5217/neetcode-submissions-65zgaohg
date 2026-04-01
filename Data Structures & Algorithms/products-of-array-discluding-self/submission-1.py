class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i in range(len(nums)): # loop through 0 to n
            product = 1
            for j in range(len(nums)): # loop through all of nums 0...to end of nums
                if i == j: # if nums at index i is equal to this n then continue
                    continue
                else: # otherwise multiplyh that element to the product
                    product *= nums[j]
            output.append(product)
            product = 1

        return output