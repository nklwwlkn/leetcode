class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        for k in s_counter:
            if k not in t_counter or t_counter[k] != s_counter[k]:
                return False

        return True 
        