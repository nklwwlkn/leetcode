class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        zero_matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        max_square_len = 0

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "1":
                    zero_matrix[r][c] = min(min(zero_matrix[r][c - 1], zero_matrix[r - 1][c]), zero_matrix[r - 1][c - 1]) + 1
                    max_square_len = max(max_square_len, zero_matrix[r][c])

        return max_square_len * max_square_len