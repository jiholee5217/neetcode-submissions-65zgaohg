class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for num, count in hashmap.items():
            freq[count].append(num)
        
        output = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                output.append(j)
                if len(output) == k:
                    return output
        
        

# To find the top k frequent elements within the array nums, we can do an algorithm
# called bucketsort. We basically group the unique integers in nums by the # of times
# they appear in the array nums aka their frequency so in order to group these, we
# first need to loop over all the numbers in nums array and put each unique number
# as a key into a hashmap and the frequency of that key as the value. 

# After that, we can iterate over the hashmap, and 

