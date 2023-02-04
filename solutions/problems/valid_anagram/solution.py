class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sizeS = len(s)
        sizeT = len(t)

        if sizeS != sizeT:
            return False
        
        hmapS = {}
        hmapT = {}

        for i in range(sizeS):
            hmapS[s[i]] = hmapS.get(s[i], 0) + 1
            hmapT[t[i]] = hmapT.get(t[i], 0) + 1
        
        for key in hmapS:
            if not key in hmapT or hmapT.get(key) != hmapS.get(key):
                return False
            
        return True
        