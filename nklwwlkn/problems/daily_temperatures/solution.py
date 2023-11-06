class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                iStack, _ = stack.pop()
                ans[iStack] = i - iStack
            stack.append([i, t])
        
        return ans