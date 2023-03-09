class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = float('-inf')
        maxEndingHere = 0

        for num in nums:
            maxEndingHere += num
            maxSoFar = max(maxSoFar, maxEndingHere)
            maxEndingHere = max(maxEndingHere, 0)
        
        return maxSoFar