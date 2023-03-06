class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        longest = 0

        l = 0
        for r in range(len(s)):
            if s[r] in hset:
                while s[r] in hset:
                    hset.remove(s[l])
                    l += 1
            longest = max(longest, (r - l + 1))
            hset.add(s[r])
        
        return longest