class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for char in s:
                i = ord(char) - ord('a')
                arr[i] += 1
            hmap[tuple(arr)].append(s)
        
        return hmap.values()