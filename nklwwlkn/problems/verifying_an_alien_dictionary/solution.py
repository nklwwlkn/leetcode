class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True
        
        charToOrder = defaultdict(int)

        for idx, char in enumerate(order):
            charToOrder[char] = idx

        for wordIdx in range(1, len(words)):
            word1 = words[wordIdx - 1]
            word2 = words[wordIdx]
            
            for charIdx in range(min(len(word1), len(word2))):
                char1 = word1[charIdx]
                char2 = word2[charIdx]

                if charToOrder[char1] < charToOrder[char2]:
                    break
                elif charToOrder[char1] > charToOrder[char2]:
                    return False

            else:
                if len(word1) > len(word2):
                    return False
                
        return True
                
