class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        totalWeight = 0
        maxWeight = float('-inf')

        for w in weights:
            if maxWeight < w:
                maxWeight = w
            totalWeight += w
        
        def canShip(cap):
            ships = 1
            currCap = cap

            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            
            return ships <= days
        
        minCap = totalWeight
        l = maxWeight
        r = totalWeight
        while l <= r:
            cap = (r - l) // 2 + l

            if canShip(cap):
                r = cap - 1
                minCap = min(minCap, cap)
            else:
                l = cap + 1
        
        return minCap

