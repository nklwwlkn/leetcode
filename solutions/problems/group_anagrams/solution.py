class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            hashed = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                hashed[index] += 1
            res[tuple(hashed)].append(s)
        
        return res.values()
        