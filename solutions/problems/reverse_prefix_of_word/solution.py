class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ""
        i = 0
        for char in word:
            prefix += char
            i += 1
            if char == ch:
                return prefix[::-1] + word[i : len(word)]
            
        return word


            