class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        l, r = 1, maxPiles
        k = maxPiles

        while l <= r:
            m = (r - l) // 2 + l
            time = 0
            for p in piles:
                time += math.ceil(p / m)
                
            if time <= h:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1

        return k
                

                



        