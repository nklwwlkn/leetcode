class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        tCounter, window = {}, {}

        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1
        
        need, have = len(tCounter), 0

        res = [-1, -1]
        resLen = float('inf')

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1 

            if char in tCounter and tCounter[char] == window[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in tCounter and window[s[l]] < tCounter[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""


        