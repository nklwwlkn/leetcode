class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCounter = 0
        hset = set()

        for num in nums:
            hset.add(num)
        
        for num in nums:
            if num - 1 not in hset:
                counter = 1
                while num + counter in hset:
                    counter += 1
                maxCounter = max(maxCounter, counter)
        
        return maxCounter