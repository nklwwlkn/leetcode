class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        s = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in s:
                l = 1
                while num + l in s:
                    l += 1
                longest = max(longest, l) 
        
        return longest