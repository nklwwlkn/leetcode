class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h <= stack[-1][1]:
                iStack, hStack = stack.pop()
                maxArea = max(maxArea, hStack * (i - iStack))
                start = iStack
            stack.append([start, h])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
        