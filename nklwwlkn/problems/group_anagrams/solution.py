class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            hashed = [0] * 26
            for char in word:
                hashed[ord(char) - ord('a')] += 1
            d[tuple(hashed)].append(word)
        
        return d.values()
            
