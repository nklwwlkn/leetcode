class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        l, r = 1, maxPiles
        k = maxPiles

        while l <= r:
            speed = (r - l) // 2 + l

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / speed)
            
            if totalTime <= h:
                k = min(k, speed)
                r = speed - 1
            else:
                l = speed + 1
        
        return k


        