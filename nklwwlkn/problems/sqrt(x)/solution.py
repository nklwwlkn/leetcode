class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = 0
        r = x // 2

        while l <= r:
            m = (r - l) // 2 + l
            curr = m ** 2

            if curr == x:
                return m
            elif x > curr:
                l = m + 1
            else:
                r = m - 1

        return r
        