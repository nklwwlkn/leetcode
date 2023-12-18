class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxFirst = float('-inf')
        maxSecond = float('-inf')
        minFirst = float('inf')
        minSecond = float('inf')

        for num in nums:
            if num > maxFirst:
                maxSecond = maxFirst
                maxFirst = num
            elif num > maxSecond:
                maxSecond = num
            
            if num < minFirst:
                minSecond = minFirst
                minFirst = num
            elif num < minSecond:
                minSecond = num

        return (maxFirst * maxSecond) - (minFirst * minSecond)

