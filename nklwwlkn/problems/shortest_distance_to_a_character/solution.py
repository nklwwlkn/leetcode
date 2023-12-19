class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [float('inf')] * len(s)

        pos = -len(s)
        for i in range(len(s)):
            char = s[i]
            if char == c:
                pos = i

            res[i] = min(res[i], abs(i - pos))
        
        pos = -len(s)
        for i in range(len(s) -1, -1, -1):
            char = s[i]
            if char == c:
                pos = i
            res[i] = min(res[i], abs(i - pos))


        return res
        
        
        
        