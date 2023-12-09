class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWords = 0
        for sentence in sentences:
            spaceCounter = 0
            for char in sentence:
                if char == " ":
                    spaceCounter += 1
                
            maxWords = max(maxWords, spaceCounter + 1)
        
        return maxWords
                     
        