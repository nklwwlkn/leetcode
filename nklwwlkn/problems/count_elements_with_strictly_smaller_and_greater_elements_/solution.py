class Solution:
    def countElements(self, nums: List[int]) -> int:
        mx = float('-inf')
        mn = float('inf')
        counter = 0

        for num in nums:
            if num > mx:
                mx = num
            if num < mn:
                mn = num
    

        for num in nums:
            if mn < num < mx:
                counter += 1

        return counter
