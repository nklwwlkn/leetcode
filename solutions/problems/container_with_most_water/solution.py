class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0

        l, r = 0, len(height) - 1

        while l < r:
            width = r - l
            if height[l] < height[r]:
                maxArea = max(maxArea, width * min(height[l], height[r]))
                l += 1
            else:
                maxArea = max(maxArea, width * min(height[l], height[r]))
                r -= 1
        
        return maxArea

        