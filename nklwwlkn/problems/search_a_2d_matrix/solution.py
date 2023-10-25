class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, (COLS * ROWS) - 1
        while l <= r:
            m = l + (r - l) // 2
            x = m // COLS
            y = m % COLS

            if target == matrix[x][y]:
                return True
            
            if target < matrix[x][y]:
                r = m - 1
            else:
                l = m + 1        

        return False
        