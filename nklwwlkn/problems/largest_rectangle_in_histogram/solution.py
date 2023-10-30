class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        longest = 0

        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                iStack, hStack = stack.pop()
                longest = max(longest, hStack * (idx - iStack))
                start = iStack
            stack.append([start, height])
        

        for i, h in stack:
            longest = max(longest, (len(heights) - i) * h)
        
        return longest
        