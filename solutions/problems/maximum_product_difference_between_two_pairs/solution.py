class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max_first = max(nums)
        nums.remove(max_first)

        max_second = max(nums)
        nums.remove(max_second)

        min_first = min(nums)
        nums.remove(min_first)
        
        min_second = min(nums)

        return (max_first * max_second) - (min_first * min_second)

