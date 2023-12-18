class Solution:
    def reverseWords(self, s: str) -> str:
        splitted = s.split()
        for idx, word in enumerate(splitted):
            splitted[idx] = self.rev(word)
        
        return " ".join(splitted)
    
    def rev(self, word):
        l = 0
        r = len(word) - 1

        word = [*word]
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        
        return "".join(word)