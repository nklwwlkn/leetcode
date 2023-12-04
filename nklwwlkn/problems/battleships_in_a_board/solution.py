class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] == ".":
                return 0

            visited.add((r, c))

            top = dfs(r + 1, c)
            right = dfs(r, c + 1)
            down = dfs(r - 1, c)
            left = dfs(r, c - 1)

            return 1


        counter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "X":
                    counter += dfs(r, c)
        
        return counter
        