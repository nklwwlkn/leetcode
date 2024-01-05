class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hm = defaultdict(int)
        
        l = 0
        for r in range(len(s)):

            while (r - l + 1) > 10: 
                l += 1

            if (r - l + 1) == 10:
                hm[s[l : r + 1]] += 1
        
        res = []
        for key, count in hm.items():
            if count > 1:
                res.append(key)

        return res