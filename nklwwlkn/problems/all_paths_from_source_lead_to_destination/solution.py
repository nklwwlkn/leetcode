class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        
        visited = set()
        cycle = set()   

        for u, v in edges:
            adjList[u].append(v)

        def dfs(node, dest):
            if node in visited:
                return True
            
            if node in cycle:
                return False
            
            if not adjList[node]:
                return node == dest
            
            cycle.add(node)
            for neigh in adjList[node]:
                if not dfs(neigh, dest):
                    return False
            
            visited.add(node)

            return True

        
        return dfs(source, destination)

            

