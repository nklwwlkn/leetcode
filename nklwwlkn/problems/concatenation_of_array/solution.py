class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] * (size * 2)

        for i in range(len(nums)):
            j = size + i
            ans[i] = nums[i]
            ans[j] = nums[i]
        
        return ans