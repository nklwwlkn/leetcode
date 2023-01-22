class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)

        if nums_len == 2:
            return [0, 1]
        
        hmap = {}

        for i in range(nums_len):
            diff = target - nums[i]
            hmap[diff] = i
        
        for i in range(nums_len):
            if nums[i] in hmap and hmap.get(nums[i]) != i:
                return [hmap.get(nums[i]), i]

        