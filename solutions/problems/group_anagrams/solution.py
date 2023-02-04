class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                k[index] += 1
            hmap[tuple(k)].append(s)
        
        return hmap.values()

            

        