class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        currentMin = float('inf')

        while l <= r:
            m = (r - l) // 2 + l
            currentMin = min(nums[m], currentMin)

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1
            
        return min(nums[l], currentMin)


        