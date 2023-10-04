class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        
        for i, val in enumerate(nums):
            lookup = target - val
            if lookup in hm:
                return [i, hm.get(lookup)]
            hm[val] = i
        
        