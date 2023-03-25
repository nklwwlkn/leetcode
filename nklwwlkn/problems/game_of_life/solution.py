class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        offsets = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        for r in range(ROWS):
            for c in range(COLS):

                # Count life neighbors:
                live_neighbors = 0
                for offset_x, offset_y in offsets:
                    row = r + offset_x
                    col = c + offset_y

                    if (row >= 0 and row < ROWS) and (col >= 0 and col < COLS) and abs(board[row][col]) == 1:
                        live_neighbors += 1

                # Rule 1 and Rule 3:
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    # -1 the cell is now dead, but originally was live:
                    board[r][c] = -1
                
                # Rule 4:
                if board[r][c] == 0 and live_neighbors == 3:
                    # 2 is now life, but originally was dead:
                    board[r][c] = 2

        # Build original representation of the board:
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] > 0:
                    board[r][c] = 1
                else:
                    board[r][c] = 0