class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = dict()
        d2 = dict()

        for i in range(len(s)):
            letterS = s[i]
            letterT = t[i]
            
            d1[letterS] = d1.get(letterS, 0) + 1
            d2[letterT] = d2.get(letterT, 0) + 1
        
        for letter in s:
            if letter not in d2 or d1.get(letter, -1) != d2.get(letter, 1):
                return False

        return True
            

        