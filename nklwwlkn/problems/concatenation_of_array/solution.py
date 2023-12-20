class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        i = 0
        while len(ans) < len(nums) * 2:
            if i >= len(nums):
                i = 0
            ans.append(nums[i])
            i += 1
        
        return ans



        