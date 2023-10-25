class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(openN, closedN, res):
            if closedN == openN == n:
                ans.append(res)
            if openN < n:
                dfs(openN + 1, closedN, res + "(")
            if closedN < openN:
                dfs(openN, closedN + 1, res + ")")

        dfs(0, 0, "")

        return ans
        