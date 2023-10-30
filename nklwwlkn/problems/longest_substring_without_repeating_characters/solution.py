class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        longest = 0 

        l = 0
        for r in range(len(s)):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest
        