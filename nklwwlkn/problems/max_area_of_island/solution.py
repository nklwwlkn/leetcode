class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            top = dfs(r + 1, c)
            right = dfs(r, c + 1)
            down = dfs(r - 1, c)
            left = dfs(r, c - 1)

            return top + right + down + left + 1




        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        
        return res
        