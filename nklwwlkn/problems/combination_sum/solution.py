class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        def backtrack(startIndex, currSum):
            if currSum == 0:
                res.append(combination.copy())
                return
            
            if currSum <= 0 or startIndex >= len(candidates):
                return

            for i in range(startIndex, len(candidates)):
                if currSum - candidates[i] < 0: continue

                combination.append(candidates[i])

                backtrack(i, currSum - candidates[i])

                combination.pop()
        
        backtrack(0, target)

        return res
        