class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = []
        count = {}
        for i in range(len(nums) + 1):
            occurences.append([])
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for num, cnt in count.items():
            occurences[cnt].append(num) 
        result = []
        for i in range(len(occurences) - 1, 0, -1):
            for num in occurences[i]:
                result.append(num)
                if len(result) == k:
                    return result
        

        
        # 1) First create a list of a list that stores unique integers at index i
        #    if that integer has i occurences in nums, we call this occurences
        #    and make this the size of nums + 1 because we need it to go from index 0
        #    to nums
        # 2) In order to calculate how many occurences of each integer there is,
        #    make a count hashmap that stores the integer as key and # of occurences
        #    as the value
        # 3) Loop through all the items in the hashmap and stored in the count hashmap
        #    in the list of a list storing integers at the # of occurences aka the 
        #    value of the hashmap, store the key
        # 4) Create a result list that will contain all the top k frequent elements
        # 5) Loop through the occurences list from the highest index to 0 and add it
        #    to results until the size of result == k then return result


