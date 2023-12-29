class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []

        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                stack.pop()

            stack.append(idx)
        
        return stack
        