class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        l = len(s)
        while l > 0:
            l -= 1
            if s[l] != " ":
                length += 1
            elif length > 0:
                return length

        return length