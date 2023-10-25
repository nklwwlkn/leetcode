class Solution:
    def findMin(self, nums: List[int]) -> int:
        currMin = float('inf')

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            currMin = min(currMin, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1 
        
        return currMin