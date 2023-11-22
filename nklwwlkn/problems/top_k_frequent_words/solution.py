class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        minHeap = []

        c = Counter(words)

        for key, value in c.items():
            minHeap.append((-value, key))

        heapq.heapify(minHeap)

        while minHeap and len(res) < k:
            count, value = heapq.heappop(minHeap)
            res.append(value)

        return res

        


        
        