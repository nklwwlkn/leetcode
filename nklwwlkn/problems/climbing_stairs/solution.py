class Solution:
    hm = { 1 : 1, 2 : 2, 3 : 3 }
    def climbStairs(self, n: int) -> int:
        if n in self.hm:
            return self.hm.get(n)
        
        self.hm[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.hm.get(n)
        