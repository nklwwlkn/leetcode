class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)
        visited = set()


        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node, destination):
            if node == destination:
                return True

            visited.add(node)

            for neighbour in adjList[node]:
                if neighbour not in visited:
                    if dfs(neighbour, destination):
                        return True

            return False
        
        return dfs(source, destination)

        