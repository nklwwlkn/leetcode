class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []

        for row in matrix:
            for element in row:
                minHeap.append(element)

        
        heapq.heapify(minHeap)

        while k:
            res = heapq.heappop(minHeap)
            k -= 1
        
        return res
        

        
            
            
            
        