class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        letters = set()
        counter = 0

        l = 0
        for r in range(len(s)):
            while (r - l + 1) > 3 or s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            if (r - l + 1) == 3: counter += 1
        

        return counter

            
            


        