class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for num, count in frequency.items():
            buckets[count].append(num)

        res = []

        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                res.append(num)

                if len(res) == k:
                    return res

