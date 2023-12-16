class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c = Counter(s)

        for char in t:
            if char not in c:
                return False
            c[char] -= 1

            if c[char] < 0:
                return False
        
        for key, value in c.items():
            if value > 0:
                return False
        
        return True

        