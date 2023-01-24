class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for s in strs:
            hashChar = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                hashChar[index] += 1
            hmap[tuple(hashChar)].append(s)

        return hmap.values()
            