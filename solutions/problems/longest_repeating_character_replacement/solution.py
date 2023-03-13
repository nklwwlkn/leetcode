class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        longest = 0

        l = 0
        for r in range(len(s)):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            if (r - l + 1) - max(charCount.values()) > k:
                charCount[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        
        return longest
            
        