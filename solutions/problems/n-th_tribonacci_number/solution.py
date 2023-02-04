class Solution:
    hashmap = {0 : 0, 1 : 1, 2 : 1}
    def tribonacci(self, n: int) -> int:
        if n in self.hashmap:
            return self.hashmap[n]
        else:
            self.hashmap[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            
            return self.hashmap[n]