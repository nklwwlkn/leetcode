class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterT = dict()
        counterS = dict()

        for i in range(len(s)):
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1
        

        for key, val in counterT.items():
            if key not in counterS or counterS[key] != val:
                return False

        return True

        