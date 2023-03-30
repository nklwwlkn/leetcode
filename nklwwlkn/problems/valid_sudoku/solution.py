class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQRS = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".": continue

                if value in ROWS[r] or value in COLS[c] or value in SQRS[(r // 3, c //3)]:
                    return False

                ROWS[r].add(value)
                COLS[c].add(value)
                SQRS[(r // 3, c // 3)].add(value)

        return True 
        