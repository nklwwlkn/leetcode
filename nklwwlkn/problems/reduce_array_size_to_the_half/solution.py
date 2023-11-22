class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        minHeap = []

        for key, value in c.items():
            minHeap.append((-value, key))

        heapq.heapify(minHeap)

        removed = 0
        counter = 0
        while removed < len(arr) // 2:
            count, item = heapq.heappop(minHeap)
            removed += abs(count)
            counter += 1

        
        return counter
            
            
        