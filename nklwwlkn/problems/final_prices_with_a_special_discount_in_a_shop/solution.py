class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                i = stack.pop()
                prices[i] = prices[i] - price 
            
            stack.append(idx)
        
        return prices

        

        
        