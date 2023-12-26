class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted = s.split()
        
        patternToS = dict()
        sToPattern = dict()

        if len(pattern) != len(splitted):
            return False
        
        for idx, pChar in enumerate(pattern):
            if (pChar not in patternToS) and (splitted[idx] not in sToPattern):
                patternToS[pChar] = splitted[idx]
                sToPattern[splitted[idx]] = pChar
            elif pChar in patternToS and patternToS[pChar] != splitted[idx]:
                return False
            elif splitted[idx] in sToPattern and sToPattern[splitted[idx]] != pChar:
                return False
          
        return True


        