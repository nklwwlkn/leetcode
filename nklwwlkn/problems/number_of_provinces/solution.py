class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        counter = 0
        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbour, isConnected_flag in enumerate(isConnected[node]):
                if isConnected_flag and neighbour not in visited:
                    dfs(neighbour)

        for i in range(len(isConnected)):
            if i not in visited:
                counter += 1
                dfs(i)


        return counter