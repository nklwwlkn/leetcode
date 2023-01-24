class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0

        hset = set()
        for num in nums:
            hset.add(num)

        for num in nums:
            if num - 1 not in hset:
                length = 1
                while num + length in hset:
                    length += 1
                counter = max(counter, length)

        return counter
        