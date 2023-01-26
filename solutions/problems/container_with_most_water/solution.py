class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1

        area = 0
        while start < end:
            width = end - start
            areaTemp = width * min(height[start], height[end])
            area = max(area, areaTemp)

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
            
        return area
        