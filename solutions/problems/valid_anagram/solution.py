class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        hmap_s = {}
        hmap_t = {}

        for i in range(s_len):
            hmap_s[s[i]] = hmap_s.get(s[i], 0) + 1
            hmap_t[t[i]] = hmap_t.get(t[i], 0) + 1
        
        for key in hmap_s:
            if hmap_s.get(key) != hmap_t.get(key):
                return False
        
        return True