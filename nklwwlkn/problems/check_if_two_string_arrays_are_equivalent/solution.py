class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        wordPointer1, charPointer1 = 0, 0
        wordPointer2, charPointer2 = 0, 0

        while wordPointer1 < len(word1) and wordPointer2 < len(word2):
            if word1[wordPointer1][charPointer1] != word2[wordPointer2][charPointer2]:
                return False

            charPointer1 += 1
            charPointer2 += 1
            
            if charPointer1 == len(word1[wordPointer1]):
                wordPointer1 += 1
                charPointer1 = 0
            
            if charPointer2 == len(word2[wordPointer2]):
                wordPointer2 += 1
                charPointer2 = 0
        
        return wordPointer1 == len(word1) and wordPointer2 == len(word2) 
        
            

        