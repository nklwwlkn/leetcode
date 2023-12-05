class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                currR, currC = q.popleft()

                directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
                for dR, dC in directions:
                    r = currR + dR
                    c = currC + dC

                    if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r, c))
            time += 1
        

        return time if fresh == 0 else -1
                    
        