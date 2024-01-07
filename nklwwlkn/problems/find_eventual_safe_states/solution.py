class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal = set()
        for i in range(len(graph)):
            if not graph[i]:
                terminal.add(i)

        visited = set()
        visiting = set()
        def dfs(node, target): 
            if node in target:
                return True

            if node in visiting:
                return False
            
            if node in visited:
                return True
            
            visiting.add(node)
            for n in graph[node]:
                if not dfs(n, target):
                    return False
            
            visiting.remove(node)
            visited.add(node)

            return True

        
        res = []
        for curr in range(len(graph)):
            if dfs(curr, terminal):
                res.append(curr)

        return res
