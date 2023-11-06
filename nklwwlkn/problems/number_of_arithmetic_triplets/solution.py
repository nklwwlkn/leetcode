class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        seen = set()

        for num in nums:
            seen.add(num)
            if num - diff in seen and num - diff * 2 in seen:
                counter += 1
        
        return counter