class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = dict()
        longest = 0

        l = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1

            while ((r - l + 1) - max(hm.values()) > k):
                hm[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest        