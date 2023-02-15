class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        hSet = set()

        for r in range(len(s)):
            while s[r] in hSet:
                hSet.remove(s[l])
                l += 1
            hSet.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest
        
