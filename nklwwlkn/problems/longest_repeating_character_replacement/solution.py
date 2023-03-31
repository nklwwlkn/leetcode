class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounter = {}
        longest = 0

        l = 0
        for r in range(len(s)):
            charCounter[s[r]] = charCounter.get(s[r], 0) + 1
            if ((r - l + 1) - max(charCounter.values())) > k:
                charCounter[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest