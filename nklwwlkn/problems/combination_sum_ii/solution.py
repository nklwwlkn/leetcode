class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        combination = []

        def backtrack(j, currSum):
            if currSum == 0:
                res.append(combination.copy())
                return

            if currSum < 0:
                return

            prev = -1
            for i in range(j, len(candidates)):
                if candidates[i] > currSum: 
                    break

                if candidates[i] == prev: 
                    continue
                
                combination.append(candidates[i])
                backtrack(i + 1, currSum - candidates[i])
                combination.pop()
                prev = candidates[i]
        
        backtrack(0, target)

        return res
