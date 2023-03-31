class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowBucket = set()
        longest = 0

        l = 0
        for r in range(len(s)):
            while s[r] in windowBucket:
                windowBucket.remove(s[l])
                l += 1  
            windowBucket.add(s[r])
            longest = max(longest, r - l + 1)
        
        return longest