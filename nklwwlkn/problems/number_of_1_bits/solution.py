class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        while n:
            digit = n & 1

            if digit:
                counter += 1
            
            n = n >> 1
        
        return counter
        