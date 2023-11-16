class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums.sort()

        def backtrack(startIndex):
            res.append(subset.copy())

            prev = None
            for i in range(startIndex, len(nums)):
                if prev == nums[i]: continue

                subset.append(nums[i])

                backtrack(i + 1)

                subset.pop()
                prev = nums[i]

        backtrack(0)

        return res
        