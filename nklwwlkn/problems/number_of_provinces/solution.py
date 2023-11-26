class Solution:    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root = [i for i in range(len(isConnected))]
        rank = [1] * len(isConnected)
                    
        def find(n):
            if n == root[n]:
                return n
            
            root[n] = find(root[n])
            
            return root[n]
        
        def connected(n1, n2):
            return find(n1) == find(n2)
        
        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)
            
            if root1 != root2:
                if rank[root1] < rank[root2]:
                    root[root1] = root2
                elif rank[root2] < rank[root1]:
                    root[root2] = root1
                else:
                    root[root2] = root1
                    rank[root1] += 1
    
        numberOfNodes = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] and not connected(i, j):
                    union(i,j)
                    numberOfNodes -= 1

        return numberOfNodes