class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        lowest = float('inf')
        secondLowest = float('inf')

        for price in prices:
            if price < lowest:
                secondLowest = lowest
                lowest = price
            elif lowest <= price <= secondLowest:
                secondLowest = price

        
        res = money - (lowest + secondLowest)

        return res if res >= 0 else money