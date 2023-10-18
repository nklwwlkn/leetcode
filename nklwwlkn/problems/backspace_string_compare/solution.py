class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sPointer = len(s) - 1
        tPointer = len(t) - 1

        sSkips = 0
        tSkips = 0

        while sPointer >= 0 or tPointer >= 0:
            while sPointer >= 0:
                if s[sPointer] == "#":
                    sSkips += 1
                    sPointer -= 1
                elif sSkips > 0:
                    sSkips -= 1
                    sPointer -= 1
                else:
                    break

            while tPointer >= 0:
                if t[tPointer] == "#":
                    tSkips += 1
                    tPointer -= 1
                elif tSkips > 0:
                    tSkips -= 1
                    tPointer -= 1
                else:
                    break

            if sPointer >= 0 and tPointer >= 0 and s[sPointer] != t[tPointer]:
                return False

            if (sPointer >= 0) != (tPointer >= 0):
                return False

            if sPointer >= 0:
                sPointer -= 1
            if tPointer >= 0:
                tPointer -= 1
        
        return True

            

            
