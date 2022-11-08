class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for char_s in s:
                arr[ord(char_s) - ord('a')] +=1            
            ans[tuple(arr)].append(s)
            
        return ans.values()
                
                