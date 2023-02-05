class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowsLen = len(matrix)
        colsLen = len(matrix[0])

        l, r = 0, (rowsLen * colsLen) - 1

        while l <= r:
            m = (r - l // 2) + l
            x = m // colsLen
            y = m % colsLen

            if target < matrix[x][y]:
                r = m - 1
            elif target > matrix[x][y]:
                l = m + 1
            else:
                return True
            
        return False

        