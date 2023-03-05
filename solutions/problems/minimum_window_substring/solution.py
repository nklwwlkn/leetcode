class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        window, tCount = {}, {}
        res, resLen = [-1, -1], float('inf')

        for char in t:
            tCount[char] = tCount.get(char, 0) + 1

        have, need = 0, len(tCount)

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in tCount and window[char] == tCount[char]:
                have += 1
            
            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1

                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float('inf') else "" 



        

        

        