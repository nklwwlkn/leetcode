class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tCounter, window = {}, {}

        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1
        
        res = [-1, -1]
        resLen = float('inf')

        need, have = len(tCounter), 0

        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in tCounter and tCounter[s[r]] == window[s[r]]:
                have += 1
            
            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in tCounter and window[s[l]] < tCounter[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""
                



        