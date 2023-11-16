from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        takenRows = defaultdict(set)
        takenCols = defaultdict(set)
        takenSqrs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = board[r][c]
                    takenRows[r].add(num)
                    takenCols[c].add(num)
                    takenSqrs[(r // 3, c // 3)].add(num)

        def backtrack(r, c):
            if c == 9:
                r += 1
                c = 0

            if r == 9:
                return True

            if board[r][c] != ".":
                return backtrack(r, c + 1)

            for i in range(1, 10):
                num = str(i)
                if num not in takenRows[r] and num not in takenCols[c] and num not in takenSqrs[(r // 3, c // 3)]:
                   
                    board[r][c] = num
                    takenRows[r].add(num)
                    takenCols[c].add(num)
                    takenSqrs[(r // 3, c // 3)].add(num)

                    if backtrack(r, c + 1):
                        return True

                    board[r][c] = "."
                    takenRows[r].remove(num)
                    takenCols[c].remove(num)
                    takenSqrs[(r // 3, c // 3)].remove(num)

            return False

        backtrack(0, 0)
