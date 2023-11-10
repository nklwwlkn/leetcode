class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size = 0
        zeros = 0

        l = 0
        for r in range(len(nums)):
            zeros += 1 if nums[r] == 0 else 0

            while zeros > 1:
                zeros -= 1 if nums[l] == 0 else 0
                l += 1
            
            size = max(size, r - l)

        return size
        