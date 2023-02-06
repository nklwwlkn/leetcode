class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hm = {}
        res = 0

        for s in stones:
            hm[s] = hm.get(s, 0) + 1

        for j in jewels:
            res += hm.get(j, 0)

        return res