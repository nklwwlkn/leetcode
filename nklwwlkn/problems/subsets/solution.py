class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(startIndex):
            res.append(subset.copy())

            for i in range(startIndex, len(nums)):
                subset.append(nums[i])

                backtrack(i + 1)

                subset.pop()

        backtrack(0)

        return res
        