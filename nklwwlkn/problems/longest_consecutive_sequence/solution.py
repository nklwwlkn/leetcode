class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)

        longest = 0
        for num in hs:
            if not num - 1 in hs:
                curr = 1
                while num + curr in hs:
                    curr += 1
                longest = max(longest, curr)

        return longest
                
        