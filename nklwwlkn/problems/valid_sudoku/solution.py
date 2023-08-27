class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        COLS = defaultdict(set)
        ROWS = defaultdict(set)
        SQRS = defaultdict(set)


        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == ".": continue

                if cell in ROWS[r] or cell in COLS[c] or cell in SQRS[(r // 3, c // 3)]:
                    return False
                ROWS[r].add(cell)
                COLS[c].add(cell)
                SQRS[(r // 3, c // 3)].add(cell)
        

        return True

        
        