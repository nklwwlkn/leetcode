class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            mask = [0] * 26
            for char in word:
                mask[ord(char) - ord('a')] += 1
            d[tuple(mask)].append(word)
        return d.values()

        