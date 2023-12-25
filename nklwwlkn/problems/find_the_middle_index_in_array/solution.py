class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for idx, num in enumerate(nums):
            if prefix == total - prefix - num:
                return idx

            prefix += num
        
        return -1
