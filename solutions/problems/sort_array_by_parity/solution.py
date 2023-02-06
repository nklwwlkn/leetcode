class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        res = []

        for num in nums:
            if num % 2 != 0:
                odd.append(num)
            else:
                even.append(num)
        
        return even + odd