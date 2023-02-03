class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_first = max(nums)
        nums.remove(max_first)
        max_second = max(nums)

        return (max_first - 1) * (max_second - 1)