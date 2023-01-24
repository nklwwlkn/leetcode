class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmap_s = {}
        hmap_t = {}
    
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            hmap_s[s_char] = hmap_s.get(s_char, 0) + 1
            hmap_t[t_char] = hmap_t.get(t_char, 0) + 1
        
        for key in hmap_s:
            if key not in hmap_t or hmap_s.get(key, 0) != hmap_t.get(key, 1):
                return False
        
        return True

        