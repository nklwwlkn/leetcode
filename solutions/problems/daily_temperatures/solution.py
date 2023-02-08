class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperaturesSize = len(temperatures)
        res = [0] * temperaturesSize
        stack = []

        for i in range(temperaturesSize):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                iStack = stack.pop()
                res[iStack] = i - iStack
            stack.append(i)
        
        return res
        