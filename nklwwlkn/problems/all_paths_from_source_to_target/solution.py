class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0]

        adjList = defaultdict(list)

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adjList[i].append(graph[i][j])

        def dfs(node, dest):
            if node == dest:
                res.append(path.copy())
                return

            for neighbour in adjList[node]:
                path.append(neighbour)
                dfs(neighbour, dest)
                path.pop()

        
        dfs(0, len(graph) - 1)

        return res

            