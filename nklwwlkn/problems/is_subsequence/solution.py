class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        l = 0 
        j = 0
        while l < len(t) and j < len(s):
            if t[l] == s[j]:
                j += 1

            l += 1

        return j == len(s)
            
        
