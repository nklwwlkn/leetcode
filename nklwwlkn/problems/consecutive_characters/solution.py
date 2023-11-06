class Solution:
    def maxPower(self, s: str) -> int:
        counter = 1
        maxCounter = 1

        for i in range(0, len(s) - 1, 1):
            if s[i] == s[i + 1]:
                counter += 1
            else:
                counter = 1
            
            maxCounter = max(maxCounter, counter)
        
        return maxCounter
        