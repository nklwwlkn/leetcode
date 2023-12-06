class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for time in times:
            time[0], time[2] = time[2], time[0]

        for w, v, u in times:
            adjList[u].append((w, v))

        minHeap = [(0, k)]
        nodeToMin = {node : float('inf') for node in range(1, n + 1)}
        nodeToMin[k] = 0

        while minHeap:
            cWeight, cNode = heapq.heappop(minHeap)

            if cWeight > nodeToMin[cNode]: continue 

            for nWeight, nNode in adjList[cNode]:
                cost = cWeight + nWeight 

                if cost < nodeToMin[nNode]:
                    heapq.heappush(minHeap, (cost, nNode))
                    nodeToMin[nNode] = cost

        res = max(nodeToMin.values())

        return res if res != float('inf') else -1


                
