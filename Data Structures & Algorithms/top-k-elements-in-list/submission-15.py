class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])

        for key, value in frequency.items():
            bucket[value].append(key)

        res = []

        for count in range(len(nums), 0, -1):
            for num in bucket[count]:
                res.append(num)
                if len(res) == k:
                    return res
      

