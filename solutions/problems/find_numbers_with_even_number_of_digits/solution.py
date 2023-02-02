class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0

        for num in nums:
            numStr = str(num)
            if len(numStr) % 2 == 0:
                counter +=1
        
        return counter