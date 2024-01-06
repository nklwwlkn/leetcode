class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited1 = set()
        visited2 = set()

        def dfs(r, c, visited):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            top = dfs(r + 1, c, visited)
            right = dfs(r, c + 1, visited)
            left = dfs(r - 1, c, visited)
            down = dfs(r, c - 1, visited)

            return 1 + top + right + left + down

        total = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited1:
                    total += dfs(r, c, visited1)
                    
        boundaries = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited2 and r in [0, ROWS - 1] or c in [0, COLS - 1]:
                    boundaries += dfs(r, c, visited2)

                    
        return total - boundaries






        