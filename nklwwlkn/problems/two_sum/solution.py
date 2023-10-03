class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i, num in enumerate(nums):
            lookup = target - num
            if lookup in d:
                return [i, d[lookup]]
            d[num] = i
            
