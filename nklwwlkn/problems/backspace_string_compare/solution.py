class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sPointer = len(s) - 1
        tPointer = len(t) - 1

        sSkip = 0
        tSkip = 0

        while sPointer >= 0 or tPointer >= 0:
            while sPointer >= 0:
                if s[sPointer] == "#":
                    sSkip += 1
                    sPointer -= 1
                elif sSkip > 0:
                    sPointer -= 1
                    sSkip -= 1
                else:
                    break

            while tPointer >= 0:
                if t[tPointer] == '#':
                    tSkip += 1
                    tPointer -= 1
                elif tSkip > 0:
                    tPointer -= 1
                    tSkip -= 1
                else:
                    break

            if sPointer >= 0 and tPointer >= 0 and s[sPointer] != t[tPointer]:
                return False
            
            if (sPointer >= 0) != (tPointer >= 0):
                return False
            
            sPointer -= 1
            tPointer -= 1

        
        return True