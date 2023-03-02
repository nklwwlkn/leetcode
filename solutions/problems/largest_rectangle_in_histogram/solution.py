class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for idx, height in enumerate(heights):
            i = idx
            while stack and height <= stack[-1][1]:
                iStack, hStack = stack.pop()
                area = max(area, (idx - iStack) * hStack)
                i = iStack
            stack.append([i, height])
        
        for i, h in stack:
            area = max(area, ((len(heights) - i) * h))
        
        return area
