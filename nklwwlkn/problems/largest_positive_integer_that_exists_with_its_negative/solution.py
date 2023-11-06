class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        N = set(nums)
        maxN = -1

        for num in nums:
            if -num in N:
                maxN = max(maxN, num)

        return maxN
