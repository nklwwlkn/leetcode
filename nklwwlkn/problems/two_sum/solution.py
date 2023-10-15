class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()

        for i, num in enumerate(nums):
            lookup = target - num
            if lookup in hm:
                return [i, hm.get(lookup)]
            hm[num] = i
