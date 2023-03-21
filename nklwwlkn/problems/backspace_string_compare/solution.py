class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.processString(s) == self.processString(t)

    def processString(self, s: str) -> bool:
        end = ""
        ignore = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '#':
                ignore += 1
                continue
            if ignore > 0:
                ignore -= 1
                i -= 1
                continue
            end += s[i]
        
        return end