class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        c = Counter()

        longest = 0
        l = 0
        for r in range(len(s)):
            c[s[r]] += 1

            while len(c) > 2:
                c[s[l]] -= 1
                if c[s[l]] == 0:
                    del c[s[l]]
                
                l += 1
            

            longest = max(longest, r - l + 1)
        
        return longest