class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0

        heights.append(0)


        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] >= height:
                iStack, hStack = stack.pop()
                largest = max(largest, hStack * (idx  - iStack))
                start = iStack
            stack.append([start, height])
        
        print(stack)



        return largest
        