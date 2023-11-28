class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        if len(grid) == 1:
            return 1 

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque([(0, 0)])

        visited = set((0,0))

        steps = 2
        while q:
            for _ in range(len(q)):
                currentR, currentC = q.popleft()

                directions = [(1, 1), (-1, 1), (1, -1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in directions:
                    r = currentR + dr
                    c = currentC + dc

                    if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and grid[r][c] == 0:
                        if r == ROWS - 1 and c == COLS - 1:
                            return steps

                        q.append((r, c))
                        visited.add((r, c))
            steps += 1
        
        return -1

        
        