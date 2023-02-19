class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [0] * len(indices)

        pos = 0
        for idx in indices:
            ans[idx] = s[pos]
            pos += 1
        
        return "".join(ans)

