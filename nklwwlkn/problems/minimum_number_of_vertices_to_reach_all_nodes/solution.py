class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        res = []

        for fr, to in edges:
            adjList[to].append(fr)
        
        for i in range(n):
            if i not in adjList:
                res.append(i)

        return res

        