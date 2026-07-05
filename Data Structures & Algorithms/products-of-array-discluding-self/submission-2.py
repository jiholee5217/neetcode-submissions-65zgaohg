class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = postfix * output[i]
            postfix = postfix * nums[i]
        return output



nums =    [ 1,  2,  4, 6 ]
output =  [48, 24, 12, 8 ]
prefix =  [ 1,  1,  2, 8 ] # prefix array calculates the product of 
postfix = [48, 24,  6, 1 ] 

# the prefix array calculates the product of all the elements in the array before
# position i 
# the postfix array calcualtes the product of all the elements in the array before
# position i starting from the end of the array going backwards
# so you can get the product of the array except itself at position i by multiplying
# the the element at i in the prefix array and the element at i in the postfix array
# because that calculates the product of all the elements in the array except the
# element at position i of the nums array
# how to make this more efficient? 
# we can just have 1 output array right and loop through twice, on the first loop
# calculate the prefix array and on the second multiply it by the postfix array
