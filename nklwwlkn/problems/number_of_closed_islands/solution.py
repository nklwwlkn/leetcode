class Solution:
    def dfsPainter(self, grid, rows, cols, r, c, visited):
        if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] != 0:
            return 
        
        visited.add((r, c))

        grid[r][c] = 1

        self.dfsPainter(grid, rows, cols, r + 1, c, visited)
        self.dfsPainter(grid, rows, cols, r, c + 1, visited)
        self.dfsPainter(grid, rows, cols, r - 1, c, visited)
        self.dfsPainter(grid, rows, cols, r, c - 1, visited)

    def dfsCounter(self, grid, rows, cols, r, c, visited):
        if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] != 0:
            return False

        visited.add((r, c))

        self.dfsCounter(grid, rows, cols, r + 1, c, visited)
        self.dfsCounter(grid, rows, cols, r, c + 1, visited)
        self.dfsCounter(grid, rows, cols, r - 1, c, visited)
        self.dfsCounter(grid, rows, cols, r, c - 1, visited)

        return True

    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        for r in range(ROWS):
            if (r, 0) not in visited and grid[r][0] == 0:
                self.dfsPainter(grid, ROWS, COLS, r, 0, visited)

            if (r, COLS - 1) not in visited and grid[r][COLS - 1] == 0:
                self.dfsPainter(grid, ROWS, COLS, r, COLS - 1, visited)

        for c in range(COLS):
            if (0, c) not in visited and grid[0][c] == 0:
                self.dfsPainter(grid, ROWS, COLS, 0, c, visited)
            
            if (ROWS - 1, c) not in visited and grid[ROWS - 1][c] == 0:
                self.dfsPainter(grid, ROWS, COLS, ROWS - 1, c, visited)

        visited = set()
        counter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 0:
                    if self.dfsCounter(grid, ROWS, COLS, r, c, visited):
                        counter += 1

        return counter
        