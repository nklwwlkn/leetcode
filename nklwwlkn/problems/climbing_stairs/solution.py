class Solution:
    hashmap = { 0 : 0, 1 : 1, 2 : 2 }
    def climbStairs(self, n: int) -> int:
        if n in self.hashmap:
            return self.hashmap[n]
        else:
            self.hashmap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.hashmap[n]