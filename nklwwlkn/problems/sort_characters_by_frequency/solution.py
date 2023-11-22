class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        c = Counter(s)
        minHeap = []

        for key, value in c.items():
            minHeap.append((-value, key))
        
        heapq.heapify(minHeap)

        while minHeap:
            count, value = heapq.heappop(minHeap)
            while count:
                res += value
                count += 1
        
        return res

        

        

            
        
