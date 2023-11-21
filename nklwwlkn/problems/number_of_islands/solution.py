class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or grid[r][c] == "0":
                return 0

            visited.add((r,c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

            return 1


        for r in range(rows):
            for c in range(cols):
                counter += dfs(r, c)
            
        
        return counter