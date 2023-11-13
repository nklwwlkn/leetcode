class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(j, currSum):
            if currSum == 0: 
                res.append(subset.copy()) 
                return

            if currSum < 0:
                return

            for i in range(j, len(candidates)):
                if candidates[i] > currSum: continue

                subset.append(candidates[i])
                backtrack(i, currSum - candidates[i])
                subset.pop()

    
        backtrack(0, target)

        return res

        