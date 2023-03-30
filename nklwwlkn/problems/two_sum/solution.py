class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for idx, num in enumerate(nums):
            lookup = target - num
            d[lookup] = idx

        for idx, num in enumerate(nums):
            if num in d and idx != d[num]:
                return [idx, d[num]]
        
        