class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCounter = Counter(s)

        length = 0
        hasOdd = False

        for key, value in charCounter.items():
            if value % 2 == 0:
                length += value
            else:
                length += value - 1
                hasOdd = True
            
        
        return length + 1 if hasOdd else length
