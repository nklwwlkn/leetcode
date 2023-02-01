class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        areaTemp = 0
        area = 0

        while left < right:
            width = right - left
            areaTemp = width * min(height[left], height[right])
            area = max(area, areaTemp)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area


        