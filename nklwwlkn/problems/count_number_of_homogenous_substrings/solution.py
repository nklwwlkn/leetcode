class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 0

        l = 0
        for r in range(len(s)):
            if s[l] == s[r]:
                res += r - l + 1
            else:
                res += 1
                l = r
         
        return res % (10**9 + 7)

        
        