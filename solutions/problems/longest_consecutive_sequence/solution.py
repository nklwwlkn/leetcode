class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
            
        counter = 0
        for num in nums:
            if not (num - 1) in hashmap and num in hashmap:
                i = 1
                while (num + i) in hashmap:
                    i += 1
                counter = max(counter, i)
        
        return counter
        