class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if value in rows[row] or value in cols[col] or value in sqrs[(row // 3, col // 3)]:
                    return False
                
                rows[row].add(value)
                cols[col].add(value)
                sqrs[(row // 3, col // 3)].add(value)
                
        
        return True