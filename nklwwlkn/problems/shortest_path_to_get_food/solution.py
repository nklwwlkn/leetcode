class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "*":
                    q.append((r, c))
                    visited.add((r, c))
                    break

        steps = 1
        while q:
            for _ in range(len(q)):
                currentR, currentC = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r = currentR + dr
                    c = currentC + dc

                    if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited:
                        if grid[r][c] == "#":
                            return steps
                        
                        if grid[r][c] == "O":
                            q.append((r, c))
                            visited.add((r, c))

            steps += 1

        return -1
        


        


                
        