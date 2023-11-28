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
            elif self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            else:
                self.root[root1] = root2
                self.rank[root1] += 1

            return True
        
        return False

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)

        logs.sort()
        
        edges = 0
        for timestamp, u, v in logs:    
            edges += 1 if uf.union(u, v) else 0
            if edges == n - 1: return timestamp
    
        return -1

            

            
            
            
        