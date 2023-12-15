class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        nums.sort()

        res = nums[k - 1] - nums[0]
        for r in range(k, len(nums)):
            res = min(res, nums[r] - nums[r - k + 1])
        
        return res
        

       



        