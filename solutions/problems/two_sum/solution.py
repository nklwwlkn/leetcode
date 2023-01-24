class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)

        if size == 2:
            return [0, 1]

        hmap = {}

        for i in range(size):
            value = nums[i]
            hmap[value] = i
        
        for i in range(size):
            find = target - nums[i]
            
            if find in hmap and hmap.get(find) != i:
                return [hmap.get(find), i]