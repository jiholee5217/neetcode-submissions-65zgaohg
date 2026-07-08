class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowDay = 0
        highDay = 0
        maxProfit = 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                cur = prices[j] - prices[i]
                maxProfit = max(cur, maxProfit)

        return maxProfit


        