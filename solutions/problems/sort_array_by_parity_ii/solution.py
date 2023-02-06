class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        res = []

        for num in nums:
            if num % 2 != 0:
                odd.append(num)
            else:
                even.append(num)
        
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])

        return res

