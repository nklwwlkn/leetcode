class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        hm = {}

        for idx in range(len(nums)):
            hm[nums[idx]] = idx
        
        maxNum = max(nums)
        nums.remove(maxNum)
        secondMaxNum = max(nums)

        return hm[maxNum] if secondMaxNum * 2 <= maxNum else -1