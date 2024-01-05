class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        res = []

        sCounter = [0] * 26
        pCounter = [0] * 26 

        for idx in range(len(p)):
            sCounter[ord(s[idx]) - ord('a')] += 1
            pCounter[ord(p[idx]) - ord('a')] += 1
        
        matches = 0
        for i in range(len(sCounter)):
            matches += 1 if sCounter[i] == pCounter[i] else 0

        l = 0
        if matches == 26:
            res.append(l)
            
        for r in range(len(p), len(s)):
            rightCharCode = ord(s[r]) - ord('a')
            sCounter[rightCharCode] += 1
            if sCounter[rightCharCode] == pCounter[rightCharCode]:
                matches += 1
            elif sCounter[rightCharCode] - 1 == pCounter[rightCharCode]:
                matches -= 1
            
            leftCharCode = ord(s[l]) - ord('a')
            sCounter[leftCharCode] -= 1
            if sCounter[leftCharCode] == pCounter[leftCharCode]:
                matches += 1
            elif sCounter[leftCharCode] + 1 == pCounter[leftCharCode]:
                matches -= 1
            
            if matches == 26:
                res.append(l + 1)
            
            l += 1

        return res