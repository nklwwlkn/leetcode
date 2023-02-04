class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        gridSize = len(grid)
        for i in range(gridSize -1, -1, -1):
            if grid[i][0] < 0:
                count += len(grid[i])
            else:
                for j in range(len(grid[i]) - 1, -1, -1):
                    if grid[i][j] < 0:
                        count += 1
                    else:
                        break


        return count