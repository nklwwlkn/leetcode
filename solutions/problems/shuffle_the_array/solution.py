class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        res = []

        while i < n:
            r = n + i 
            res.append(nums[i])
            res.append(nums[r])
            i += 1
        
        return res
            