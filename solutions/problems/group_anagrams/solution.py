class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)

        for s in strs:
            res = [0] * 26
            for char in s:
                res[ord(char) - ord('a')] += 1
            hmap[tuple(res)].append(s)
        
        return hmap.values()