class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        l, r = 1, maxPiles
        res = maxPiles

        while l <= r:
            k = ((r - l) // 2) + l

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)
            if totalTime <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res