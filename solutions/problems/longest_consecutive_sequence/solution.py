class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        hset = set(nums)
        counter = 1

        for num in nums:
            if num - 1 not in hset:
                longest = 1
                while num + longest in hset:
                    longest += 1
                counter = max(counter, longest)
        
        return counter