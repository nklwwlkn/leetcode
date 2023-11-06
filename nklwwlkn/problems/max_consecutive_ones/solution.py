class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tempCons = 0
        maxCons = 0
        
        for num in nums:
            if num == 1:
                tempCons += 1
                maxCons = max(tempCons, maxCons)
            else:
                tempCons = 0
    
        return maxCons