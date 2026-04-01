class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        # iterate through the list 
        # for each unique number in the list, use it as the key in a hashmap
        # and if it is in the list then increment by 1 and if not then
        # make it become 1 
        for n in nums:
            result[n] += 1

        top_k = sorted(result.items(), key=lambda x: x[1], reverse=True)[:k]
        top_keys = [key for key, val in top_k]

        return top_keys