class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = dict()
        t_to_s = dict()
       
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if not char_s in s_to_t and not char_t in t_to_s:
               s_to_t[char_s] = char_t
               t_to_s[char_t] = char_s
            elif s_to_t.get(char_s) != char_t or t_to_s.get(char_t) != char_s:
                return False
        
        return True
                