class Solution:
    hashmap = { 0 : 0, 1 : 1 }
    def fib(self, n: int) -> int:
        if n in self.hashmap:
            return self.hashmap[n]
        else: 
            self.hashmap[n] = self.fib(n - 1) + self.fib(n - 2)
            return self.hashmap[n]