class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter = 0
        
        for word in words:
            if len(word) >= len(pref):
                if word[0:len(pref)] == pref:
                    counter += 1
    
        return counter