class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = dict()

        for idx in range(len(nums)):
            d1[nums[idx]] = idx

        for idx in range(len(nums)):
            find = target - nums[idx]
            if find in d1 and idx != d1[find]:
                return [d1[find], idx]