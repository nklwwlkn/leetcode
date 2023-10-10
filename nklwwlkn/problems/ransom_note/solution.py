class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmR = dict()
        hmM = dict()

        for char in ransomNote:
            hmR[char] = hmR.get(char, 0) + 1

        for char in magazine:
            hmM[char] = hmM.get(char, 0) + 1
        

        for char in ransomNote:
            if not char in hmM or hmM.get(char) < hmR.get(char):
                return False
        
        return True

        