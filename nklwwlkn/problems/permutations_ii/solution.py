class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []

        nums.sort()

        def backtrack(j, nums):
            if j == len(nums):
                res.append(permutation.copy())
                return

            visited = set()
            for i in range(j, len(nums)):
                if nums[i] not in visited:

                    permutation.append(nums[i])
                    visited.add(nums[i])
                    nums[i], nums[j] = nums[j], nums[i]

                    backtrack(j + 1, nums)

                    nums[i], nums[j] = nums[j], nums[i]
                    permutation.pop()
                
        
        backtrack(0, nums)

        return res