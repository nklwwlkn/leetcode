class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c = defaultdict(int)

        counter = 0
        l = 0
        for r in range(len(s)):
            c[s[r]] += 1

            while "a" in c and "b" in c and "c" in c:
                counter += len(s) - r

                c[s[l]] -= 1

                if c[s[l]] == 0:
                    del c[s[l]]
                
                l += 1 
        

        return counter
                
        