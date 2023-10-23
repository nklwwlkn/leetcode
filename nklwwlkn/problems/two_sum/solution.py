class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()

        for idx, num in enumerate(nums):
            lookup = target - num
            if lookup in hm:
                return [idx, hm.get(lookup)]
            hm[num] = idx
        