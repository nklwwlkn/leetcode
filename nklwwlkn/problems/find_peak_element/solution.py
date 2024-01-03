class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        def isPeak(idx):
            isGreaterToLeft = (idx == 0) or nums[idx] >= nums[idx - 1]
            isGreaterToRight = (idx == len(nums) - 1) or nums[idx] >= nums[idx + 1]

            return isGreaterToLeft and isGreaterToRight

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l

            if isPeak(m):
                return m
            
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1


        return -1


        