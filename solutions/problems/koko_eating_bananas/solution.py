class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = max(piles)
        l, r = 1, maxK
        k = maxK

        while l <= r:
            speed = (r - l) // 2 + l

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / speed)
            
            if totalTime <= h:
                r = speed - 1
                k = min(k, speed)
            else:
                l = speed + 1
        
        return k

        