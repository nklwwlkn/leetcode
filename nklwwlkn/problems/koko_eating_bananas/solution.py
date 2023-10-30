class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)

        l, r = 1, maxPiles

        speed = maxPiles

        while l <= r:
            m = l + (r - l) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / m)
            
            if time <= h:
                speed = min(speed, m)
                r = m - 1
            else:
                l = m + 1


        return speed