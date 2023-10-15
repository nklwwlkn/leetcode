class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterS, counterT = dict(), dict()

        for i in range(len(s)):
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1


        for key, value in counterS.items():
            if not key in counterT or counterT.get(key) != value:
                return False

        return True
