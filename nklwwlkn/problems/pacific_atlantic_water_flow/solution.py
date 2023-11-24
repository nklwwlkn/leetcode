class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or prev > heights[r][c]:
                return 

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])


        for c in range(COLS):
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
            dfs(0, c, pac, heights[0][c])

        for r in range(ROWS):
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
            dfs(r, 0, pac, heights[r][0])

        return pac.intersection(atl)
        