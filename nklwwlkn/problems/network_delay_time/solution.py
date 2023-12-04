class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for source, target, cost in times:
            adjList[source].append((cost, target))
        
        nodeToMin = {node : float('inf') for node in range(1, n + 1)}

        minHeap = [(0, k)]
        nodeToMin[k] = 0

        while minHeap:
            currentCost, currentNode = heapq.heappop(minHeap)

            if currentCost > nodeToMin[currentNode]:
                continue
            
            for nCost, nNode in adjList[currentNode]:
                cost = currentCost + nCost

                if cost < nodeToMin[nNode]:
                    nodeToMin[nNode] = cost
                    heapq.heappush(minHeap, (cost, nNode))
        


        res = max(nodeToMin.values())

        return res if res != float('inf') else -1
        