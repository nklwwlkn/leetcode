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
        size = len(points)

        edges = []
        for i in range(size):
            for j in range(i, size):
                if i != j:
                    a = points[i]
                    b = points[j]
                    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])

                    edges.append([distance, i, j])
        
        edges.sort()

        uf = UnionFind(size)

        minCost = 0
        edgesUsed = 0
        
        for distance, u, v in edges:
            if not uf.isConnected(u, v):
                uf.union(u, v)
                minCost += distance
                edgesUsed += 1

                if edgesUsed == size - 1:
                    break
            
        return minCost