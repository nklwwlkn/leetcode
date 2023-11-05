class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)

        speed = maxPiles

        l, r = 1, maxPiles
        
        while l <= r:
            m = l + (r - l) // 2
            
            time = 0
            for p in piles:
                time += math.ceil(p / m)

            if time <= h:
                r = m - 1
                speed = min(speed, m)
            else:
                l = m + 1
        
        return speed 