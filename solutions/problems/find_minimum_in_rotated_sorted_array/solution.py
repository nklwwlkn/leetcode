class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        currentMin = float('inf')

        while l <= r:
            m = (r - l) // 2 + l
            currentMin = min(currentMin, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
            
        return min(currentMin, nums[l])
        