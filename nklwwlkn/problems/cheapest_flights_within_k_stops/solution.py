class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        costs = []

        for fr, to, cost in flights:
            adjList[fr].append((cost, to))

        minHeap = [(0, src, 0)]
        minCost = {}

        while minHeap:
            cCost, cNode, cStops = heapq.heappop(minHeap)

            if cNode in minCost and minCost[cNode] <= cStops:
                continue

            minCost[cNode] = cStops

            if cNode == dst:
                return cCost
            
            if cStops <= k:
                for nCost, nNode in adjList[cNode]:
                    heapq.heappush(minHeap, (cCost + nCost, nNode, cStops + 1))

        return -1
        