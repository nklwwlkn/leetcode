class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap_s = {}
        hmap_t = {}

        for i in range(len(s)):
            val_s = s[i]
            val_t = t[i]
            hmap_s[val_s] = hmap_s.get(val_s, 0) + 1
            hmap_t[val_t] = hmap_t.get(val_t, 0) + 1

        for key in hmap_s:
            if key not in hmap_t or hmap_s[key] != hmap_t[key]:
                return False
        
        return True


        