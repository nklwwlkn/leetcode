class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        hmap = {}
        nums_len = len(nums)

        for i in range(nums_len):
            hmap[nums[i]] = i

        for i in range(nums_len):
           find = target - nums[i]
           if find in hmap and i != hmap.get(find):
               return [i, hmap.get(find)]
            

        