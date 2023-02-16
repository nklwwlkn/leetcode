class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProfit = 0

        for price in prices:
            if price < lowest:
                lowest = price
            maxProfit = max(maxProfit, price - lowest)
        
        return maxProfit