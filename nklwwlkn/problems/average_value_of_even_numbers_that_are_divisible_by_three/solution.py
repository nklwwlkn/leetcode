class Solution:
    def averageValue(self, nums: List[int]) -> int:
        counter = 0
        total = 0

        for num in nums:
            if num % 3 == 0 and num % 2 == 0:
                counter += 1
                total += num
        
        return total // counter if total else 0