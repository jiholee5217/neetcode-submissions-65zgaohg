class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set() # created a hashset
        
        for i in range(len(nums)): # iterate through all of nums
            if nums[i] in hashSet: # if 
                return True
            else: 
                hashSet.add(nums[i])
        
        return False
        
        # create a hashset and iterate through nums.
        # if the integer is in the hashset, then return false
        # otherwise add the integer to the hashset and move to the next
        # one
         