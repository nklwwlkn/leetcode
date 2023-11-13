class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def backtrack(i, currSum):
            if currSum == 0: 
                res.append(subset.copy()) 
                return

            if i >= len(candidates) or currSum < 0:
                return

            # Pick it:
            subset.append(candidates[i])
            currSum -= candidates[i]
            backtrack(i, currSum)

            # Not Pick it:
            subset.pop()
            currSum += candidates[i]
            backtrack(i + 1, currSum)
    
        backtrack(0, target)

        return res

        