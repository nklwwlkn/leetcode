class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.calcNumericValue(firstWord) + self.calcNumericValue(secondWord) == self.calcNumericValue(targetWord)
    
    def calcNumericValue(self, word: str) -> int:
        res = ""
        for char in word:
            res += str(ord(char) - ord('a'))
        
        return int(res)
