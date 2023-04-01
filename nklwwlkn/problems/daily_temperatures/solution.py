class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [idx, temp]
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idxStack, tempStack = stack.pop()
                res[idxStack] = idx - idxStack

            stack.append([idx, temp])
        
        return res
