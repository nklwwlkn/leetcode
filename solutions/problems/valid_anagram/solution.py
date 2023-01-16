class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap_s = {}
        hmap_t = {}

        for i in range(len(s)):
            if s[i] not in hmap_s:
                hmap_s[s[i]] = 1
            else:
                hmap_s[s[i]] += 1

            if t[i] not in hmap_t:
                hmap_t[t[i]] = 1
            else:
                hmap_t[t[i]] += 1
            
        
        for char in hmap_s:
            if char not in hmap_t or hmap_t[char] != hmap_s[char]:
                return False

        return True
        
    