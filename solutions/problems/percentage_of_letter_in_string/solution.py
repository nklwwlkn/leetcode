class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        hm = {}

        for char in s:
            hm[char] = hm.get(char, 0) + 1

        return 0 if letter not in hm else int(hm.get(letter) / len(s) * 100)