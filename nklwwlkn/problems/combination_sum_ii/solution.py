class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        candidates.sort()

        def backtrack(startIndex, currSum):
            if currSum == 0:
                res.append(combination.copy())
                return

            if currSum < 0 or startIndex >= len(candidates):
                return

            prev = None
            for i in range(startIndex, len(candidates)):
                if prev == candidates[i]: continue

                if currSum - candidates[i] < 0: break

                combination.append(candidates[i])

                backtrack(i + 1, currSum - candidates[i])

                combination.pop()
                prev = candidates[i]

        
        backtrack(0, target)

        return res
        