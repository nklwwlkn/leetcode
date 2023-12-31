class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, (rows * cols) - 1


        while l <= r:
            m = l + (r - l) // 2

            x = m // cols
            y = m % cols

            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                l = m + 1
            else:
                r = m - 1


        return False
        