class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        distance = 0
        for i in range(len(points) - 1):
            a, b = points[i], points[i + 1]
            distance += max(abs(a[0] - b[0]), abs(a[1] - b[1]))

        return distance            
        