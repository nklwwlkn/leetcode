class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
  
        def dfs(r, c, grid):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0: return 0
    
            visited.add((r,c))
      
            return 1 + dfs(r + 1, c, grid) + dfs(r - 1, c, grid) + dfs(r, c + 1, grid) + dfs(r, c - 1, grid)  
  
        maximum_island_size = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maximum_island_size = max(maximum_island_size, dfs(r, c, grid))
        return maximum_island_size