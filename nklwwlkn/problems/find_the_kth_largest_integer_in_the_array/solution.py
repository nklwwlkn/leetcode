class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []

        for num in nums:
            heapq.heappush(heap, int(num))
            while len(heap) > k:
                heapq.heappop(heap)

        return str(heap[0])