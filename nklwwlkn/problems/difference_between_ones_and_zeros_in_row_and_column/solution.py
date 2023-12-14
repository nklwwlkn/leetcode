class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        onesRow = defaultdict(int)
        onesCol = defaultdict(int)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    onesRow[r] += 1
                    onesCol[c] += 1

        for r in range(ROWS):
            for c in range(COLS):
                grid[r][c] = onesRow[r] + onesCol[c] - (ROWS - onesRow[r]) - (COLS - onesCol[c])
    
        return grid
        