class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hset = set()

        for char in s:
            if char in hset:
                return char
            hset.add(char)