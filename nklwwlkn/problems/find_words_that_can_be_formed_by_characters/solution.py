class Solution:
    def __init__(self):
        self.cache = {}

    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCounter = Counter(chars)
        goodStrings = 0

        for word in words:
            if word not in self.cache:
                wordCounter = Counter(word)
                wordLength = len(word)
                for char, count in wordCounter.items():
                    if charsCounter[char] < count:
                        wordLength = 0
                        break
                self.cache[word] = wordLength
            goodStrings += self.cache[word]
    
        return goodStrings



        
        