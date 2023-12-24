class Solution:
    def minOperations(self, s: str) -> int:
        patternA = 0
        patternB = 0

        for idx, char in enumerate(s):
            if idx % 2 == 0:
                if char != "0":
                    patternA += 1
                if char != "1":
                    patternB += 1 
            else:
                if char != "0":
                    patternB += 1
                if char != "1":
                    patternA += 1 

        
        return min(patternA, patternB)
        
            
