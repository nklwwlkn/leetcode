class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, n):
        if n == self.root[n]:
            return n
        
        self.root[n] = self.find(self.root[n])

        return self.root[n]

    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)

    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            elif self.rank[root2] < self.rank[root1]:
                self.root[root2] = root1
            else:
                self.root[root1] = root2
                self.rank[root1] += 1
            
            return True
        
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        size = len(points)

        for i in range(size):
            for j in range(i + 1, size):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)

                edges.append((cost, i, j))

        
        edges.sort()
        
        uf = UnionFind(size)

        minCost = 0
        numberOfConnections = 0
        for w, u, v in edges:
            if not uf.isConnected(u, v):
                uf.union(u, v)
                minCost += w
                numberOfConnections += 1
            
            if size - 1 == numberOfConnections: break 

        return minCost

