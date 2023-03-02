class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(openN, closeN, stack):
            if openN == n == closeN:
                return res.append("".join(stack))
            if openN < n:
                backtrack(openN + 1, closeN, stack + ["("])
            if closeN < openN:
                backtrack(openN, closeN + 1, stack + [")"])
        
        backtrack(0,0,[])

        return res


        