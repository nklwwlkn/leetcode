class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        N = set()
        for num in nums:
            if num in N:
                return True
            else:
                N.add(num)

        return False
        
        