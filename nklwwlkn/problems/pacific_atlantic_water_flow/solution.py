class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac = set()
        atl = set()
        
        def dfs(r, c, visited, prev = None):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or (prev and heights[r][c] < prev):
                return

            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        
        for r in range(ROWS):
            dfs(r, COLS - 1, atl)
            dfs(r, 0, pac)

        for c in range(COLS):
            dfs(ROWS - 1, c, atl)
            dfs(0, c, pac)

        return pac.intersection(atl)

        


            
