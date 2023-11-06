class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            num = nums[i]
            hm[num] = i

        for i in range(len(nums)):
            find = target - nums[i]
            
            if find in hm and i != hm.get(find):
                return [i, hm.get(find)]

            
        