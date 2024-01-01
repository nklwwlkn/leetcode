class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        l = 2
        r = num // 2

        while l <= r:
            m = (r - l) // 2 + l
            res = m ** 2

            if res == num:
                return True
            elif res < num:
                l = m + 1
            else:
                r = m - 1

        return False