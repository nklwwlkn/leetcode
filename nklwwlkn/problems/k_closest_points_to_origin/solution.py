class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            x, y = point
            dist = -sqrt(pow(x, 2) + pow(y, 2))

            if len(minHeap) == k:
                heapq.heappushpop(minHeap, (dist, x, y))
            else:
                heapq.heappush(minHeap, (dist, x, y))
        

        return [[x, y] for (dist, x, y) in minHeap]


        