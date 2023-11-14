class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        
        nums.sort()

        def backtrack(j):
            res.append(subset.copy())

            prev = float('-inf')
            for i in range(j, len(nums)):
                if prev == nums[i]: continue

                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
                prev = nums[i]

        backtrack(0)

        return res            
            
        