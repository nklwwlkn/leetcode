class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []

        def backtrack(j):
            if j >= len(nums):
                res.append(permutation.copy())
                return
            
            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                permutation.append(nums[j])

                backtrack(j + 1)

                nums[i], nums[j] = nums[j], nums[i]
                permutation.pop()

        
        backtrack(0)

        return res
        