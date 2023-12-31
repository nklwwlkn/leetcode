class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] == "X":
                return 
            
            board[r][c] = "P"
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == 'O':
                    dfs(r, c)
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "P":
                    board[r][c] = "O"