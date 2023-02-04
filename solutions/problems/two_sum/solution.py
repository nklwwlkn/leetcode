class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSize = len(nums)

        if numsSize == 2:
            return [0, 1]
        
        hmap = {}

        for i in range(numsSize):
            find = target - nums[i]
            hmap[find] = i
        
        for i in range(numsSize):
            if nums[i] in hmap and hmap.get(nums[i], -1) != i:
                return [i, hmap.get(nums[i])]
