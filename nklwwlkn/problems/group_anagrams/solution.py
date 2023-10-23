class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs:
            h = [0] * 26
            for char in word:
                h[ord(char) - ord('a')] += 1
            hm[tuple(h)].append(word)
        
        return hm.values()
        