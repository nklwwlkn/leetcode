class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap_s = {}
        hashmap_t = {}
        
        for char_s in s:
            hashmap_s[char_s] = hashmap_s.get(char_s, 0) + 1
        
        for char_t in t:
            hashmap_t[char_t] = hashmap_t.get(char_t, 0) + 1
            
    
        for char_s in s:
            if hashmap_s.get(char_s) != hashmap_t.get(char_s):
                return False
            
        return True