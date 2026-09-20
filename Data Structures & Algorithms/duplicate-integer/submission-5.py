class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = set()

        for num in nums:
            if num in exist:
                return True
            else:
                exist.add(num)

        return False

    # Time Complexity: O(n) where n is the sie of the nums list 
    # Space Complexity: O(n) where n is the size of nums list