class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                iStack, hStack = stack.pop()
                maxArea = max(maxArea, (i - iStack) * hStack)
                start = iStack
            stack.append([start, h])

        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea
        