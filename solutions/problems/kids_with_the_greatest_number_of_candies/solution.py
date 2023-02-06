class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        maxC = max(candies)

        for c in candies:
            if c + extraCandies >= maxC:
                res.append(True)
            else:
                res.append(False)

        return res