class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        splitted = sentence.split(' ')
        word = -1

        for i, w in enumerate(splitted):
            if w.startswith(searchWord):
                return i + 1
            
        return word
                