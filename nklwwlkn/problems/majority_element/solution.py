class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = None

        for num in nums:
            if count <= 0:
                res = num
            
            count = count + 1 if num == res else count - 1
        
        return res
        