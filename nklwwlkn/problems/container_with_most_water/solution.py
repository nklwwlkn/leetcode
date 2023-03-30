class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            width = r - l

            if height[l] < height[r]:
                maxArea = max(maxArea, width * height[l])
                l += 1
            else:
                maxArea = max(maxArea, width * height[r])
                r -= 1

        return maxArea

        