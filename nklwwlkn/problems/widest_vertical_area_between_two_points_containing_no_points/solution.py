class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        if len(points) == 2:
            return points[1][0] - points[0][0]
        
        xPoints = sorted([point[0] for point in points])
        maxDistance = 0
        for r in range(1, len(xPoints)):
            leftX = xPoints[r - 1]
            rightX = xPoints[r]

            maxDistance = max(maxDistance, rightX - leftX)

        return maxDistance
