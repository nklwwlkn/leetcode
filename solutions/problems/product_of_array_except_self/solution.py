class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [1] * size

        prefix = 1
        for i in range(size):
            ans[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(size -1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans