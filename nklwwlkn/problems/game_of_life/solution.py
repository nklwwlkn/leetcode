class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        offsets = [(1,0), (0,1), (-1, 0), (0, -1), (1, 1), (-1,-1), (1,-1), (-1,1)]

        for r in range(ROWS):
            for c in range(COLS):
                live_neighbors = 0
                for offset_r, offset_c in offsets:
                    row = r + offset_r
                    col = c + offset_c

                    if (row >= 0 and row < ROWS) and (col >= 0 and col < COLS) and abs(board[row][col]) == 1:
                        live_neighbors += 1
                
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0

        