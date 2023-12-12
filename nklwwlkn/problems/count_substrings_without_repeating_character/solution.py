class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        counter = 0
        window = set()

        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])

            counter += r - l + 1
        
        return counter
            
        