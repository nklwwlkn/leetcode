class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                if value in rows[r] or value in cols[c] or value in sqrs[(r // 3, c // 3)]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                sqrs[(r // 3, c //3)].add(value)
        return True
                
        