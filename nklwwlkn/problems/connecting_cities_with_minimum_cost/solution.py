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
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        for connection in connections:
            connection[0], connection[2] = connection[2], connection[0]

        connections.sort()

        uf = UnionFind(n + 1)

        edgesUsed = 0
        minCost = 0
        for cost, u, v in connections:
            if uf.union(u, v):
                edgesUsed += 1
                minCost += cost

            if edgesUsed == n - 1:
                break

        return minCost if (minCost and edgesUsed == n - 1) else -1 

